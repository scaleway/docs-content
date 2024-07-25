import os

# TODO merge create_concepts_list function and replace_concepts function

# This function turns a string into kebab case (kebab-case-is-like-this) for anchor links, for instance Public flexible IP adress -> #public-flexible-ip-address
def to_kebab_case(value):
    return "-".join(value.lower().split())


# This function retrieves the concepts of a product and , and store them as a list of list ([concept1, url1], [concept2, url2])
def create_concepts_list(product):
  # gets current working directory
  directory_path=os.getcwd()
  global concepts_list
  concepts_list = []
  for dirpath, dirnames, filenames in os.walk(f"{directory_path}/{product}"):
    for filename in filenames:
      if filename.endswith("concepts.mdx"):
        file_path=f"{dirpath}/{filename}"
        # print(file_path)
        with open(file_path, 'r') as file:  
          for line in file:
            concept_specs = []
            if line.startswith("## "):
              # Removes "## " at the begining of concept line, and appends it the concept to concept_specs
              concept_specs.append(line.strip("# \n").lower())
              # Creates the relative path and appends it to concept_specs
              relative_path = file_path.removeprefix(directory_path).removesuffix(".mdx") + "/#" + to_kebab_case(line.strip("# \n"))
              concept_specs.append(relative_path)
              # Appends the list of concept specs (concept + link) to concepts_list
              concepts_list.append(concept_specs)
  return concepts_list

# TODO Create a function that takes a specific product (= subfolder such as object, functions, instances, etc. in contents) and walks the pages of this product to look for the first ocurrence of each concept, checks if the line contains a link to the concept (if line contains slug then skip), and if not, replaces the concept with "[concept](link to concept)".

def replace_concepts(product):
  # gets current working directory
  directory_path=os.getcwd()
  # create absolute path to product folder with cwd (path/to/docs/content) + category and product path from user input (e.g. serverless/jobs or compute/instances)
  product_path = f"{directory_path}/{product}"
  for dirpath, dirnames, filenames in os.walk(product_path):
    for filename in filenames:
      file_path=f"{dirpath}/{filename}"
      with open(file_path, 'r+') as file:
        # Exclude product index files and concepts files (obviously)

        if filename.endswith(".mdx") and filename != "index.mdx" and filename != "concepts.mdx":
          # add a first_ocurrence_replaced = False, and set it to True after replacement, and if True, break replacement "if" block to switch to next concept in the list
          data = file.readlines()
          for line in data:
            # TODO Exclude frontmatter from line read/replace (if line starts with stuff from frontmatter or other method)
            for concept in concepts_list:
              first_ocurrence_replaced = 0
              # look for concept in concepts list, and replace concept with [concept](URL) if match.
              if concept[0] in line and first_ocurrence_replaced == 0 :
                # TODO find a way to avoid errors with concepts that contain another concept ("permission" and "permission set" for instance), like: if concept

                line_index = data.index(line)
                new_line = line.replace(concept[0], f"[{concept[0]}]({concept[1]})")
                data[line_index] = new_line
                first_ocurrence_replaced = 1
                print(new_line)


# create_concepts_list(input("Enter a category and product, e.g. \'compute/instances\' :"))
create_concepts_list("serverless/jobs")
            
replace_concepts("serverless/jobs")
