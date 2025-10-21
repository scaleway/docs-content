import os
import logging
from slack_sdk import WebClient
from datetime import timedelta, date, datetime
import re
import ast

DEFAULT_VAL_FREQ = 6
FILEPATH = "./" ## for local testing use "../" and shift filepath_list[] indexes +1

def convert_to_date_and_delta(val_date, val_freq):
    "Converts validation date string to datetime and validation frequency string (months) to timedelta."
    try:
        val_date_conv = datetime.strptime(val_date.rstrip('\n'), '%Y-%m-%d').date()
        val_freq_conv = timedelta(days=int(val_freq) * 30.4)
        return val_date_conv, val_freq_conv
    except ValueError:
        # handles the case where validation format is incorrect
        return None, None

def get_prod_cat_ref():
    "Makes a dictionary where keys are product slugs and values are their category label and product label"

    product_categories = {}

    # Read the menu file
    with open(FILEPATH + "menu/navigation.ts", "r", encoding="utf-8") as f:
        js = f.read()

    # remove all lines up to "export default"
    js = re.sub(r"^import .*", "", js, flags=re.M)          # remove import lines
    js = re.sub(r"//.*", "", js)                            # strip line comments
    js = re.sub(r"/\*.*?\*/", "", js, flags=re.S)           # strip block comments
    js = js.replace("export default", "").strip()           # strip "export default" and cleanup

    # Replace only unquoted menu/icon references

    # Convert items - [accountMenu, billingMenu] → ['account', 'billing']
    js = re.sub(r"\b([a-zA-Z0-9_]+)Menu\b(?!')", r"'\1'", js)

    # Convert icons - OrganizationDashboardCategoryIcon → 'OrganizationDashboardCategory'
    js = re.sub(r"\b([A-Z][A-Za-z0-9]+)Icon\b(?!')", r"'\1'", js)

    # Normalize JS → Python syntax ---
    js = re.sub(r"(\w+):", r"'\1':", js)                    # quote keys
    js = js.replace("null", "None")                         # replace nulls with Nones
    js = re.sub(r",(\s*[}\]])", r"\1", js)                  # remove trailing commas

    # Convert the js string now containing Python literal syntax, into an actual Python object.
    data = ast.literal_eval(js)

    # Helper function
    def camel_to_kebab(name: str) -> str:
        """Convert camelCase or PascalCase to kebab-case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)
        return s2.lower()

    # Helper function
    def prettify_label(slug: str) -> str:
        """Convert kebab-case to title case."""
        return slug.replace("-", " ").title()

    # Walk structure and make new dict

    product_categories = {}

    for section in data:
        for category in section["items"]:
            category_label = category["label"]
            for item in category["items"]:
                key = camel_to_kebab(item).lower().replace("_", "-")
                label = prettify_label(key)
                product_categories[key] = [category_label, label]

    return(product_categories)


def needs_review(val_date, val_freq):
    "Returns true if doc needs to be reviewed, based on val date and frequency"
    val_date_conv, val_freq_conv = convert_to_date_and_delta(val_date, val_freq)
    if val_date_conv is None or val_freq_conv is None:
        return False
    today = date.today()
    # calculate how long since doc was reviewed, in days
    delta = today - val_date_conv
    # return true or false depending on evaluation of data
    return delta >= val_freq_conv

def extract_metadata(filepath):
    "Extracts validation date and validation frequency from a document."
    with open(filepath) as doc:
        meta_limiters = 0
        has_val_date = False
        val_freq = DEFAULT_VAL_FREQ

        for line in doc:
            if "validation: " in line:
                val_date = line.split(": ", 1)[1].strip()
                has_val_date = True
            if "validation_frequency:" in line:
                val_freq = line.split(": ", 1)[1].strip()
            if "---" in line:
                meta_limiters += 1
            # once two --- strings are found, it is the end of the meta section, stop checking file
            if meta_limiters >= 2:
                break
                
    return has_val_date, val_date if has_val_date else None, val_freq

def process_files(directory):
    "Processes files in the content directory to check for those needing review."
    print("Processing files to check for those needing review")
    docs_to_review=[]
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith(".mdx"):
                has_val_date, val_date, val_freq = extract_metadata(filepath)
                if has_val_date and needs_review(val_date, val_freq):
                    docs_to_review.append(filepath)
    return docs_to_review

def get_doc_cat_name(filepath, prod_cat_ref):
    "Returns a document-to-review's category and tidied-up filepath, based on its raw filepath and the prod_cat_ref dict."
    trimmed_filepath = filepath[2:-4]
    filepath_list = trimmed_filepath.split("/")

    if filepath_list[0] == "tutorials":
        category_product = "Tutorials"
    else:
        # catches everything in pages
        category = prod_cat_ref.get(filepath_list[1], ["Unknown", "Unknown"])[0]
        product = prod_cat_ref.get(filepath_list[1], ["Unknown", "Unknown"])[1]
        category_product = category + ": " + product
        
    return category_product, trimmed_filepath

def organize_docs_by_category(docs_to_review):
    "Organizes docs to review by category into a dictionary."
    print("Organizing docs by category")
    dict_by_cat = {}
    
    # one shot: make a dict of all products and their categories, based on menu file
    prod_cat_ref = get_prod_cat_ref()
    
    for filepath in docs_to_review:
        category_product, trimmed_filepath = get_doc_cat_name(filepath, prod_cat_ref)

        if category_product not in dict_by_cat:
            dict_by_cat[category_product] = [trimmed_filepath]
        else:
            dict_by_cat[category_product].append(trimmed_filepath)
    
    # sort the dictionary alphabetically by category
    dict_by_cat_sorted = {key: value for key, value in sorted(dict_by_cat.items())}

    return dict_by_cat_sorted

def prep_message(docs_to_review_by_cat):
    "Prepares the message to sent to the Slack channel, containing the docs to review"
    print("Preparing message")
    message = ":wave: Hi doc team, here are some docs to review: \n \n"

    for key in docs_to_review_by_cat:
        message += "*" + key + "*" + "\n"
        for doc in docs_to_review_by_cat[key]:
            message += doc + "\n"
        message += "\n"
    print(message)
    return(message)

def send_message(message):
    "Sends the message containing docs to review to the Slack channel"
    print("Sending message")
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    client.chat_postMessage(
        channel = "#review-doc",
        text = message,
        username = "DocReviewBot"
    )

def main():
    docs_to_review = process_files(FILEPATH)
    docs_to_review_by_cat = organize_docs_by_category(docs_to_review)
    message = prep_message(docs_to_review_by_cat)
    #if os.environ.get("DRY_RUN") != "true":
    #    send_message(message)
    print(message)

if __name__ == "__main__":
    main()