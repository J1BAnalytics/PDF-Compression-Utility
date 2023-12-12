# Usage Guide

This guide provides step-by-step instructions on how to use the PDF compression tool.

## Getting Started

1. **Clone the Repository:**
   - Clone the repository to your local machine:
     ```bash
     git clone <repository_URL>
     cd PDF-Compression-Tool
     ```

2. **Install Dependencies:**
   - Ensure you have Python installed.
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

## Compression Process

1. **Prepare PDF Files:**
   - Place the PDF files you want to compress in the `input_pdfs` directory.

2. **Run the Compression Script:**
   - Execute the compression script using the Docker container or locally:
     ```bash
     # Docker container (after building the image)
     docker run -v "$(pwd)/input_pdfs:/app/input_pdfs" -v "$(pwd)/compressed_pdfs:/app/compressed_pdfs" <image_name>

     # Locally (if not using Docker)
     python scripts/compress_pdf.py
     ```

3. **Retrieve Compressed PDFs:**
   - Once the compression process is complete, find the compressed PDF files in the `compressed_pdfs` directory.
