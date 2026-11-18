import os
import re
import sys
import requests

CATALOG_URL = "https://api.scaleway.com/product-catalog/v2alpha1/public-catalog/products"
DOC_FILE_PATH = "pages/generative-apis/reference-content/supported-models.mdx"

TASK_MAPPING = {
    "chat": "Text",
    "code": "Code",
    "vision": "Vision",
    "ocr": "OCR",
    "embeddings": "Embeddings",
    "audio_transcription": "Audio"
}

def format_anchor(name: str) -> str:
    """Generates the Markdown anchor, e.g., 'glm-5.3' -> '[glm-5.3](#glm-53)'"""
    clean_anchor = re.sub(r"[^a-zA-Z0-9\-]", "", name).lower()
    return f"[{name}](#{clean_anchor})"

def format_modalities(tasks: list) -> str:
    """Maps API tasks to clean labels for the documentation."""
    modalities = []
    for t in tasks:
        val = TASK_MAPPING.get(t.lower(), t.capitalize())
        if val not in modalities:
            modalities.append(val)
    return ", ".join(modalities) if modalities else "Text"

def get_target_h2_section(tasks: list) -> str:
    """Routes to one of the 7 model categories based on tasks."""
    task_set = set(t.lower() for t in tasks)

    # 1. Multimodal Text + Audio
    if "audio_transcription" in task_set and "chat" in task_set:
        return r"##\s*Multimodal models\s*\(Text and audio\)"
    
    # 2. Audio Transcription
    elif "audio_transcription" in task_set:
        return r"##\s*Audio transcription models"
    
    # 3. OCR Models
    elif "ocr" in task_set:
        return r"##\s*OCR models"
    
    # 4. Multimodal Text + Vision
    elif "vision" in task_set:
        return r"##\s*Multimodal models\s*\(Text and vision\)"
    
    # 5. Embeddings Models
    elif "embeddings" in task_set:
        return r"##\s*Embeddings models"
    
    # 6. Code Models (specific code without chat)
    elif "code" in task_set and "chat" not in task_set:
        return r"##\s*Code models"
    
    # 7. Text Models (chat, standard text)
    else:
        return r"##\s*Text models"

def fetch_catalog_models():
    """Fetches all models from the Catalog API while handling pagination."""
    models = {}
    page = 1
    page_size = 100

    while True:
        res = requests.get(
            CATALOG_URL,
            params={"product_types": "generative_apis", "page": page, "page_size": page_size}
        )
        res.raise_for_status()
        data = res.json()
        
        for item in data.get("products", []):
            name = item.get("product")
            if not name:
                continue
                
            props = item.get("properties", {}).get("generative_apis", {})
            if name not in models:
                models[name] = {
                    "name": name,
                    "provider": props.get("provider_name", "Unknown"),
                    "status": item.get("status", "general_availability"),
                    "tasks": props.get("tasks", []),
                    "reasoning": props.get("reasoning", False),
                    "reasoning_values": props.get("supported_reasoning_values", [])
                }

        if page * page_size >= data.get("total_count", 0):
            break
        page += 1

    return models

def clean_name_for_comparison(row_str: str) -> str:
    """Extracts raw model name from a markdown row for comparison only."""
    cells = [c.strip() for c in row_str.strip().strip("|").split("|")]
    if not cells:
        return ""
    match = re.search(r"\[([^\]]+)\]", cells[0])
    val = match.group(1) if match else cells[0]
    return val.strip().lower()

def insert_row_alphabetically_in_table(content: str, heading_pattern: str, new_rows_with_names: list) -> str:
    """Inserts rows into an already-sorted table at their exact alphabetical position without altering other rows."""
    if not new_rows_with_names:
        return content

    match_heading = re.search(rf"(?m)^{heading_pattern}\s*$", content, re.IGNORECASE)
    if not match_heading:
        print(f"⚠️ Heading not found with pattern: {heading_pattern}")
        return content

    heading_end = match_heading.end()
    rest = content[heading_end:]

    table_match = re.search(r"(\n(?:\s*\|[^\n]+\|\s*\n)+)", rest)
    if not table_match:
        print(f"⚠️ No table found under: {heading_pattern}")
        return content

    table_lines = [line.strip() for line in table_match.group(1).strip().split("\n") if line.strip()]
    if len(table_lines) < 2:
        return content

    header_lines = table_lines[:2]
    data_rows = list(table_lines[2:])

    sorted_new_items = sorted(new_rows_with_names, key=lambda x: x["name"].lower())

    for item in sorted_new_items:
        new_row_str = item["row_str"]
        new_name_key = item["name"].lower()
        
        inserted = False
        for i, existing_row in enumerate(data_rows):
            existing_name_key = clean_name_for_comparison(existing_row)
            if new_name_key < existing_name_key:
                data_rows.insert(i, new_row_str)
                inserted = True
                break
        
        if not inserted:
            data_rows.append(new_row_str)

    updated_table = "\n" + "\n".join(header_lines + data_rows) + "\n"
    new_rest = rest[:table_match.start(1)] + updated_table + rest[table_match.end(1):]
    return content[:heading_end] + new_rest

def append_to_markdown_table_under_heading(content: str, heading_pattern: str, new_rows: list) -> str:
    """Appends new rows to the end of the table (used for EOL models)."""
    if not new_rows:
        return content

    match_heading = re.search(rf"(?m)^{heading_pattern}\s*$", content, re.IGNORECASE)
    if not match_heading:
        print(f"⚠️ Heading not found with pattern: {heading_pattern}")
        return content

    heading_end = match_heading.end()
    rest = content[heading_end:]

    table_match = re.search(r"(\n(?:\s*\|[^\n]+\|\s*\n)+)", rest)
    if not table_match:
        print(f"⚠️ No table found under: {heading_pattern}")
        return content

    raw_table = table_match.group(1).rstrip()
    rows_to_add = "\n" + "\n".join(new_rows)
    updated_table = raw_table + rows_to_add + "\n"

    new_rest = rest[:table_match.start(1)] + updated_table + rest[table_match.end(1):]
    return content[:heading_end] + new_rest

def generate_model_detail_block(model: dict) -> str:
    """Generates the '###' technical card for an active model."""
    name = model["name"]
    title = name.capitalize()
    provider = model["provider"]
    
    reasoning_vals = model.get("reasoning_values", [])
    reasoning_str = ", ".join(f"`{r}`" for r in reasoning_vals) if reasoning_vals else "None"

    tasks = model.get("tasks", [])
    has_vision = any(t in tasks for t in ["vision", "ocr"])
    image_formats = "PNG, JPEG, WebP" if has_vision else "N/A"

    hf_org = provider.replace(" ", "")
    hf_link = f"[{name}](https://huggingface.co/{hf_org}/{name})"

    return (
        f"### {title}\n\n"
        f"<!-- TODO: Add a 1-2 sentence description for {name} -->\n\n"
        f"| Attribute | Value |\n"
        f"|-----------|-------|\n"
        f"| Provider | {provider} |\n"
        f"| Supports structured output | TBD |\n"
        f"| Supports function calling | TBD |\n"
        f"| Supports parallel tool-calling | TBD |\n"
        f"| Supported reasoning efforts | {reasoning_str} |\n"
        f"| Supported image formats | {image_formats} |\n"
        f"| Supported languages | TBD |\n"
        f"| Maximum output (tokens) - Serverless | TBD |\n"
        f"| Hugging Face model card | {hf_link} |"
    )

def insert_detail_block_into_section(content: str, heading_pattern: str, detail_block: str) -> str:
    """Inserts the ### detail card at the end of the target H2 section, right before the next H2."""
    match_heading = re.search(rf"(?m)^{heading_pattern}\s*$", content, re.IGNORECASE)
    if not match_heading:
        print(f"⚠️ Section not found: {heading_pattern}. Adding at end of document.")
        return content + "\n\n" + detail_block + "\n"

    section_start = match_heading.end()
    rest = content[section_start:]

    next_h2_match = re.search(r"(?m)^##\s+", rest)
    if next_h2_match:
        insert_pos = next_h2_match.start()
        new_rest = rest[:insert_pos].rstrip() + "\n\n" + detail_block + "\n\n" + rest[insert_pos:]
        return content[:section_start] + new_rest
    else:
        return content.rstrip() + "\n\n" + detail_block + "\n"

def main():
    if not os.path.exists(DOC_FILE_PATH):
        print(f"❌ File not found: {DOC_FILE_PATH}")
        sys.exit(1)

    print("1. Fetching models from the Catalog API...")
    catalog = fetch_catalog_models()
    print(f"   {len(catalog)} models fetched in total.")

    with open(DOC_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_active_items = []
    new_eol_rows = []
    active_models_to_insert = []
    added_summary = []

    for m in catalog.values():
        name = m["name"]
        status = m["status"]

        # Completely skip retired models
        if status == "retired":
            print(f"  ⏭️ Ignored (retired model) : {name}")
            continue

        # If the model is already present on the page, leave it untouched
        if name.lower() in content.lower():
            continue

        # Only 'end_of_life' models go to the EOL table
        if status == "end_of_life":
            new_eol_rows.append(f"| {m['provider']} | `{name}` | TBD | TBD | TBD |")
            added_summary.append(f"- **EOL** : `{name}` ({m['provider']})")
            print(f"  ➕ Detected for EOL : {name}")
        else:
            name_anchor = format_anchor(name)
            modalities = format_modalities(m["tasks"])
            row_str = f"| {name_anchor} | Yes | {modalities} | TBD | TBD |"
            
            new_active_items.append({"name": name, "row_str": row_str})
            active_models_to_insert.append(m)
            added_summary.append(f"- **Active** : `{name}` ({m['provider']})")
            print(f"  ➕ Detected for Active : {name}")

    if not new_active_items and not new_eol_rows:
        print("✅ Documentation is already in sync with the catalog.")
        sys.exit(0)

    # 1. Insert new active models at their exact alphabetical position in '## Models technical summary'
    content = insert_row_alphabetically_in_table(
        content,
        r"##\s*Models technical summary",
        new_active_items
    )

    # 2. Insert each '###' card into its respective H2 category
    for m in active_models_to_insert:
        target_h2 = get_target_h2_section(m["tasks"])
        detail_block = generate_model_detail_block(m)
        content = insert_detail_block_into_section(content, target_h2, detail_block)
        print(f"  📌 Card inserted for `{m['name']}` under : {target_h2}")

    # 3. Append EOL models to the end of '## End of life (EOL) models' without sorting
    content = append_to_markdown_table_under_heading(
        content,
        r"##\s*End[- ]of[- ]life.*models",
        new_eol_rows
    )

    with open(DOC_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n📝 {DOC_FILE_PATH} updated successfully.")

    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as sf:
            sf.write("### 🤖 New models detected in the catalog\n\n")
            sf.write("\n".join(added_summary) + "\n\n")
            sf.write("> ⚠️ Remember to complete descriptions and `TBD` before merging the PR.\n")

if __name__ == "__main__":
    main()