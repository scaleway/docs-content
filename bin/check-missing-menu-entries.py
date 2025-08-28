import os
import json

PAGES_DIR = "pages"
NAV_FILE = "menu/navigation.json"

def get_mdx_files(root):
    mdx_files = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".mdx"):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, root)
                # Exclude index.mdx and troubleshooting
                if filename == "index.mdx":
                    continue
                if "/troubleshooting/" in rel_path.replace("\\", "/"):
                    continue
                # Exclude files directly in the pages folder
                if os.path.dirname(rel_path) == "":
                    continue
                mdx_files.append(rel_path)
    return mdx_files

def get_slugs_from_nav(nav_json):
    slugs = set()
    def extract(obj):
        if isinstance(obj, dict):
            if "slug" in obj:
                slugs.add(obj["slug"])
            for v in obj.values():
                extract(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item)
    extract(nav_json)
    return slugs

def main():
    # Load navigation.json
    with open(NAV_FILE, "r", encoding="utf-8") as f:
        nav_json = json.load(f)
    nav_slugs = get_slugs_from_nav(nav_json)

    # Get all relevant mdx files
    mdx_files = get_mdx_files(PAGES_DIR)

    # Check which files are missing from navigation
    missing = []
    nav_slug_filenames = set()
    for slug in nav_slugs:
        # Extract the last part of the slug (filename without extension)
        slug_filename = slug.split('/')[-1].split('?')[0].split('#')[0]
        slug_filename = os.path.splitext(slug_filename)[0]
        nav_slug_filenames.add(slug_filename)

    for mdx in mdx_files:
        filename = os.path.splitext(os.path.basename(mdx))[0]
        if filename not in nav_slug_filenames:
            missing.append(mdx)

    print("MDX files missing from navigation.json:\n")
    for m in missing:
        file_path = os.path.join(PAGES_DIR, m)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            if "noindex: true" in content:
                print(f"{m}  [noindex: true]")
            else:
                print(m)
        except Exception as e:
            print(f"{m}  [error reading file: {e}]")

if __name__ == "__main__":
    main()