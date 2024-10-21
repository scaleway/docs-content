import os


class AddLinkOnFirstConcept:


  def __init__(self):
    pass


  def to_kebab_case(self, value):
      return "-".join(value.lower().split())


  def select_folder_to_process(self):
     product=input("enter the product to process (in the \"category/product\" format: ")
     return product


  # This function retrieves the concepts of a product and , and store them as a list of list ([concept1, url1], [concept2, url2])
  def create_concepts_list(self, product):
    # gets current working directory
    directory_path=os.getcwd()
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
                concept_anchor = file_path.removeprefix(directory_path).removesuffix(".mdx") + "/#" + self.to_kebab_case(line.strip("# \n"))
                concept_specs.append(concept_anchor)
                # Appends the list of concept specs (concept + concept_anchor) to concepts_list
                concepts_list.append(concept_specs)
    return concepts_list


  def create_files_to_update_list(self, product):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(product):
      for filename in filenames:
        if filename.endswith(".mdx") and filename != "index.mdx" and filename != "concepts.mdx":
          file_path = f"{dirpath}/{filename}"
          files_list.append(file_path)      
    return files_list
  

  def check_if_concept_in_other_concept(concepts_list):
    concepts = concepts_list
    control_list = concepts_list
    skip_concept = False

    for i in concepts:
      for j in control_list:
        if i in j:
          skip_concept = True
          print(f"Concept \"{i}\" is contained in \n{j}\n")
          return skip_concept

  # Working implementation
  def replace_string_in_file(self, current_file, old_string, new_string):
    with open(current_file, "r+") as file_to_process:
      content = file_to_process.read()
      new_content = content.replace(old_string, new_string, 1)
      file_to_process.seek(0)
      file_to_process.truncate(0)
      print(file_to_process)
      file_to_process.write(new_content)
      return

  # Version with line-by-line processing
  def line_by_line_replace(self, current_file, old_string, new_string):
    with open(current_file, "r") as file_to_process:
      lines_of_file = file_to_process.readlines()
    # iterates over each line of the file
    for i in range(len(lines_of_file)):
      if old_string in lines_of_file[i]:
        # replace concept once in the line 
        lines_of_file[i] = lines_of_file[i].replace(old_string, new_string, 1)
        break
    with open(current_file, "w") as file_to_write:
      file_to_write.writelines(lines_of_file)
    return

  def replace(self):
      # product = self.select_folder_to_process()
      product = "serverless/jobs"
      concepts_list = self.create_concepts_list(product)
      files_list = self.create_files_to_update_list(product)
      # Looks for each concept in each page
      for file in files_list:
        for concept in concepts_list:
          skip_concept = False
          old_string = concept[0]
          new_string = f"[{concept[0]}]({concept[1]})"
          current_file=file
          # Check if concept already has link to concepts page
          with open(file) as file_to_check:
            if new_string not in file_to_check.read() and skip_concept == False:
              self.line_by_line_replace(current_file, old_string, new_string)
              # Add test new content and error handling before printing line below
              print(f"{old_string} replaced by {new_string} in file {file}.")
            else:
              print(f"{new_string} already in {file_to_check}")
          file_to_check.close()
      return


# TODO

# - DONE - Check if concept is already present in file before replacing

# - Add tests

# - Address case where concept is part of another concept (e.g. "serverless" and "Serverless Framework")

# - Make sure capitalized concepts are properly matched and reproduced

# - Try a different replace method using readlines(), then looping through each line to search for concept and easily exclude frontmatter

#   - Frontmatter:
#     - Enter frontmatter section: If current_line contains "---\n" then switch
#       on frontmatter_check = True
#     - If frontmatter_check = True and current_line == "---\n" then switch off
#       frontmatter_check = False
#     - If frontmatter_check = True then skip line
#   
#   - Code block:
#     - Same as frontmatter but with "```"

#   - Monospace
#     - if concept is between "`[any string]`" and "`[any string]`" then DO NOT skip line
#       as 
#     - if concept is between "`[any string]" and "[any string]`" then skip line

# To check programmatically if a markdown string is monospace or bold or italics, ChatGPT provides the answer below:

# Example in Python with markdown-it-py:

# You can use the markdown-it-py library to parse the Markdown into tokens and inspect them to detect different formatting.
# Install the library:

# bash

# pip install markdown-it-py

# Code Example:

# python

# from markdown_it import MarkdownIt

# # Function to check markdown formatting
# def check_formatting(markdown_text):
#     md = MarkdownIt()
#     tokens = md.parse(markdown_text)
    
#     for token in tokens:
#         if token.type == 'inline':
#             for child in token.children:
#                 if child.type == 'code_inline':
#                     print("Monospace text:", child.content)
#                 elif child.type == 'strong_open':
#                     print("Bold text detected")
#                 elif child.type == 'em_open':
#                     print("Italics text detected")

# # Example usage
# markdown_string = "Here is some **bold** text, *italics*, and `monospace` code."

# check_formatting(markdown_string)

# Explanation:

#     The MarkdownIt parser breaks down the Markdown string into tokens.
#     We loop through these tokens and check for specific types (code_inline for inline monospace, strong_open for bold, and em_open for italics).

# Output:

# scss

# Bold text detected
# Italics text detected
# Monospace text: monospace

# Parsing Bold, Italics, and Monospace

#     Monospace (inline code) is detected by the code_inline token.
#     Bold text is detected by strong_open and strong_close tokens.
#     Italics text is detected by em_open and em_close tokens.

# This approach allows you to programmatically check for these specific formatting patterns in any Markdown string.
