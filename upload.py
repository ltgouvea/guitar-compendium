# This is what I've become now. Half-man, half-machine.

import os
import shutil
from pathlib import Path
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from datetime import datetime

# Caminhos base do projeto
ROOT_DIR = Path(".").resolve()
TMP_DIR = ROOT_DIR / "tmp"
CONTENT_DIR = ROOT_DIR / "content" / "compendium"
COVER_DIR = ROOT_DIR / "static" / "cover"
PDFS_DIR = ROOT_DIR / "static" / "pdfs"

# Certifique-se que os diretórios de destino existem
CONTENT_DIR.mkdir(parents=True, exist_ok=True)
COVER_DIR.mkdir(parents=True, exist_ok=True)
PDFS_DIR.mkdir(parents=True, exist_ok=True)

def parse_pdf_date(date_str):
    if not date_str or not date_str.startswith("D:"):
        return "Desconhecida"
    date_str = date_str[2:]
    
    # Tenta os formatos mais comuns
    formats = [
        "%Y%m%d%H%M%S%z",        # com timezone
        "%Y%m%d%H%M%S",          # sem timezone
        "%Y%m%d",                # só data
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            continue

    return "Desconhecida"

def extract_metadata(pdf_path):
    reader = PdfReader(str(pdf_path))
    info = reader.metadata or {}

    return {
        "Author": info.get("/Author", "Desconhecido"),
        "CreationDate": parse_pdf_date(info.get("/CreationDate", "")),
        "Creator": info.get("/Creator", "Desconhecido"),
        "ModDate": parse_pdf_date(info.get("/ModDate", "")),
        "Producer": info.get("/Producer", "Desconhecido"),
        "Title": info.get("/Title", pdf_path.stem)
    }

def create_markdown(metadata, md_path, pdf_filename):
    md_content = f"""---
title: '{metadata.get("Title", "")}'
weight: 1
bookcase_cover_src: 'cover/{pdf_filename}.png'
bookcase_cover_src_dark: 'cover/{pdf_filename}.png'
download_link: '/pdfs/{pdf_filename}.pdf'
---

- Author: {metadata.get("Author", "Desconhecido")}
- CreationDate: {metadata.get("CreationDate", "Desconhecida")}
- Creator: {metadata.get("Creator", "Desconhecido")}
- ModDate: {metadata.get("ModDate", "Desconhecida")}
- Producer: {metadata.get("Producer", "Desconhecido")}
- Title: {metadata.get("Title", "Desconhecido")}

{{< button >}}
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

def extract_cover(pdf_path, output_path):
    images = convert_from_path(str(pdf_path), first_page=1, last_page=1)
    if images:
        images[0].save(str(output_path), "PNG")

def process_pdf(pdf_path):
    pdf_filename = pdf_path.stem
    print(f"Processando: {pdf_filename}")

    # Cria pasta para o markdown
    book_dir = CONTENT_DIR / pdf_filename
    book_dir.mkdir(parents=True, exist_ok=True)

    # Extrai metadados
    metadata = extract_metadata(pdf_path)

    # Cria markdown
    md_path = book_dir / f"{pdf_filename}.md"
    create_markdown(metadata, md_path, pdf_filename)

    # Extrai imagem da capa
    cover_output_path = COVER_DIR / f"{pdf_filename}.png"
    extract_cover(pdf_path, cover_output_path)

    # Move PDF
    shutil.move(str(pdf_path), PDFS_DIR / f"{pdf_filename}.pdf")

def main():
    pdf_files = list(TMP_DIR.glob("*.pdf"))
    if not pdf_files:
        print("Nenhum PDF encontrado em /tmp.")
        return

    for pdf_path in pdf_files:
        process_pdf(pdf_path)

if __name__ == "__main__":
    main()
