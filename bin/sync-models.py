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
    """Génère l'ancre Markdown, ex : 'glm-5.3' -> '[glm-5.3](#glm-53)'"""
    clean_anchor = re.sub(r"[^a-zA-Z0-9\-]", "", name).lower()
    return f"[{name}](#{clean_anchor})"

def format_modalities(tasks: list) -> str:
    """Mappe les tâches de l'API vers des libellés propres pour la doc."""
    modalities = []
    for t in tasks:
        val = TASK_MAPPING.get(t.lower(), t.capitalize())
        if val not in modalities:
            modalities.append(val)
    return ", ".join(modalities) if modalities else "Text"

def get_target_h2_section(tasks: list) -> str:
    """Route vers l'une des 7 catégories de modèles selon les tâches."""
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
    
    # 6. Code Models (spécifique code sans chat)
    elif "code" in task_set and "chat" not in task_set:
        return r"##\s*Code models"
    
    # 7. Text Models (chat, text standard)
    else:
        return r"##\s*Text models"

def fetch_catalog_models():
    """Récupère l'ensemble des modèles de l'API Catalog en gérant la pagination."""
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

def append_to_markdown_table_under_heading(content: str, heading_pattern: str, new_rows: list) -> str:
    """Ajoute les nouvelles lignes à la fin du premier tableau sous un titre donné."""
    if not new_rows:
        return content

    match_heading = re.search(rf"(?m)^{heading_pattern}\s*$", content, re.IGNORECASE)
    if not match_heading:
        print(f"⚠️ Titre introuvable avec le motif : {heading_pattern}")
        return content

    heading_end = match_heading.end()
    rest = content[heading_end:]

    table_match = re.search(r"(\n(?:\s*\|[^\n]+\|\s*\n)+)", rest)
    if not table_match:
        print(f"⚠️ Aucun tableau trouvé sous : {heading_pattern}")
        return content

    raw_table = table_match.group(1).rstrip()
    rows_to_add = "\n" + "\n".join(new_rows)
    updated_table = raw_table + rows_to_add + "\n"

    new_rest = rest[:table_match.start(1)] + updated_table + rest[table_match.end(1):]
    return content[:heading_end] + new_rest

def generate_model_detail_block(model: dict) -> str:
    """Génère la fiche technique '###' pour un modèle actif."""
    name = model["name"]
    title = name.capitalize()
    provider = model["provider"]
    
    # Formatage des efforts de reasoning
    reasoning_vals = model.get("reasoning_values", [])
    reasoning_str = ", ".join(f"`{r}`" for r in reasoning_vals) if reasoning_vals else "None"

    # Formats d'image si vision ou ocr
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
    """Insère la fiche détaillée ### à la fin de la section H2 ciblée, juste avant le prochain H2."""
    match_heading = re.search(rf"(?m)^{heading_pattern}\s*$", content, re.IGNORECASE)
    if not match_heading:
        print(f"⚠️ Section introuvable : {heading_pattern}. Ajout en fin de document.")
        return content + "\n\n" + detail_block + "\n"

    section_start = match_heading.end()
    rest = content[section_start:]

    # Recherche du titre H2 suivant qui délimite la fin de la section actuelle
    next_h2_match = re.search(r"(?m)^##\s+", rest)
    if next_h2_match:
        insert_pos = next_h2_match.start()
        new_rest = rest[:insert_pos].rstrip() + "\n\n" + detail_block + "\n\n" + rest[insert_pos:]
        return content[:section_start] + new_rest
    else:
        # Dernier H2 du document
        return content.rstrip() + "\n\n" + detail_block + "\n"

def main():
    if not os.path.exists(DOC_FILE_PATH):
        print(f"❌ Fichier non trouvé : {DOC_FILE_PATH}")
        sys.exit(1)

    print("1. Récupération des modèles depuis l'API Catalog...")
    catalog = fetch_catalog_models()
    print(f"   {len(catalog)} modèles récupérés au total.")

    with open(DOC_FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_active_rows = []
    new_eol_rows = []
    active_models_to_insert = []
    added_summary = []

    for m in catalog.values():
        name = m["name"]
        
        # Si le modèle est déjà présent dans la page, on ne le touche pas
        if name.lower() in content.lower():
            continue

        if m["status"] in ["end_of_life", "retired"]:
            new_eol_rows.append(f"| {m['provider']} | `{name}` | TBD | TBD | TBD |")
            added_summary.append(f"- **EOL/Retired** : `{name}` ({m['provider']})")
            print(f"  ➕ Détecté pour EOL : {name}")
        else:
            name_anchor = format_anchor(name)
            modalities = format_modalities(m["tasks"])
            new_active_rows.append(f"| {name_anchor} | Yes | {modalities} | TBD | TBD |")
            
            # Stocke le modèle actif pour insertion dans la bonne section H2
            active_models_to_insert.append(m)
            added_summary.append(f"- **Actif** : `{name}` ({m['provider']})")
            print(f"  ➕ Détecté pour Actif : {name}")

    if not new_active_rows and not new_eol_rows:
        print("✅ La documentation est déjà synchronisée avec le catalogue.")
        sys.exit(0)

    # 1. Mise à jour du tableau technique sous '## Models technical summary'
    content = append_to_markdown_table_under_heading(
        content,
        r"##\s*Models technical summary",
        new_active_rows
    )

    # 2. Insertion de chaque fiche '###' dans sa catégorie H2 respective
    for m in active_models_to_insert:
        target_h2 = get_target_h2_section(m["tasks"])
        detail_block = generate_model_detail_block(m)
        content = insert_detail_block_into_section(content, target_h2, detail_block)
        print(f"  📌 Fiche insérée pour `{m['name']}` sous : {target_h2}")

    # 3. Mise à jour du tableau EOL sous '## End of life (EOL) models'
    content = append_to_markdown_table_under_heading(
        content,
        r"##\s*End[- ]of[- ]life.*models",
        new_eol_rows
    )

    with open(DOC_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n📝 {DOC_FILE_PATH} mis à jour avec succès.")

    # Synthèse pour la PR dans GitHub Actions
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as sf:
            sf.write("### 🤖 Nouveaux modèles détectés dans le catalogue\n\n")
            sf.write("\n".join(added_summary) + "\n\n")
            sf.write("> ⚠️ Pensez à compléter les descriptions et les valeurs `TBD` avant de fusionner la PR.\n")

if __name__ == "__main__":
    main()