# How It Works

The PDF compression tool uses the PyPDF2 library to reduce the file size of PDF documents while preserving their content and quality.

## Compression Technique

1. **Content Stream Compression:**
   - PyPDF2's `compressContentStreams` method is used to compress the content streams of the PDF pages, reducing the file size.

2. **Quality Reduction:**
   - The tool applies quality reduction techniques to minimize the file size while attempting to maintain acceptable visual quality.

## Algorithm Overview

- The script iterates through each page of the input PDF file, compresses the content streams, and writes the compressed output to a new PDF file.
