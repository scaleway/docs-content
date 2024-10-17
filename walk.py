import os
import fileinput, sys

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

  def replace_string_in_file(file_path, old_string, new_string):
        with open(file_path, "r") as current_file:
          content = current_file.read()
          file.close()

        # Replace the old string with the new string
        new_content = content.replace(old_string, new_string, 1)

        # Open the file in write mode to overwrite with new content
        with open(file_path, 'w') as file:
              file.write(new_content)
              file.close()

        return

  def replace(self):
      # product = self.select_folder_to_process()
      product = "serverless/jobs"
      concepts_list = self.create_concepts_list(product)
      files_list = self.create_files_to_update_list(product)
      for file in files_list:
        for concept in concepts_list:
          old_string = concept[0]
          new_string = f"[{concept[0]}]({concept[1]})"
      self.replace_string_in_file(file, old_string, new_string)

      return
