import os
import re

def extract_title(frontmatter):
    title_match = re.search(r'title:\s*(.+)', frontmatter)
    if title_match:
        return title_match.group(1).strip('"').strip("'")
    return None

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        frontmatter_end = content.find('---', 3)
        if frontmatter_end != -1:
            frontmatter = content[3:frontmatter_end].strip()
            title = extract_title(frontmatter)
            if title:
                return f"[{title}]({file_path})"
    return None

def main():
    pages_file = 'pages/pages-ts.md'
    with open(pages_file, 'r', encoding='utf-8') as file:
        pages_content = file.readlines()

    page_paths = []
    for line in pages_content:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('---'):
            page_paths.append(line)

    page_list = []
    for page_path in page_paths:
        full_path = os.path.join(os.path.dirname(pages_file), page_path)
        page_entry = process_file(full_path)
        if page_entry:
            page_list.append(page_entry)

    for entry in page_list:
        print(entry)

if __name__ == "__main__":
    main()