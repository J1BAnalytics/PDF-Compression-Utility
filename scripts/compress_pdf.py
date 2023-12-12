import PyPDF2
import os

def compress_pdf(input_path, output_path):
    # Check if the input directory exists
    if not os.path.exists(input_path):
        print(f"Input directory '{input_path}' does not exist.")
        return

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Iterate through the files in the input directory
    for filename in os.listdir(input_path):
        if filename.endswith('.pdf'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            # Open the input PDF file
            with open(input_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                pdf_writer = PyPDF2.PdfWriter()

                # Iterate through each page and add it to the writer
                for page_num in range(pdf_reader.numPages):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Compress the PDF by reducing its quality
                pdf_writer.compressContentStreams(squeeze=True)

                # Write the compressed PDF to the output file
                with open(output_file, 'wb') as output:
                    pdf_writer.write(output)
                    print(f"File '{filename}' compressed successfully.")

# Input and output directories
input_directory = 'input_pdfs'
output_directory = 'compressed_pdfs'

# Call the compress function with the input and output directories
compress_pdf(input_directory, output_directory)
