import pdfplumber
import regex as re
import os
from PyPDF2 import PdfReader, PdfWriter

def divide_pdf(input_pdf_path, page_ranges):
    # Create a directory to store divided PDFs
    output_dir = "../PDF Files"
    #os.makedirs(output_dir, exist_ok=True)

    # Read the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)

        # Divide the PDF into multiple PDFs based on specified page ranges
        for i, (start, end) in enumerate(page_ranges):
            if start < 0 or start >= total_pages or end < start or end > total_pages:
                raise ValueError("Invalid page range specified.")

            writer = PdfWriter()
            # Add pages to the new PDF
            for page_num in range(start, end):
                writer.add_page(reader.pages[page_num])
            
            
            # Write the new PDF to file
            output_pdf_path = "../PDF Files/Direito_Processual_Penal_Divided" + f"_Parte_{i + 1}.pdf"
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)

    print(f"PDF divided into {len(page_ranges)} parts in '{output_dir}'.")

# Example usage:
page_ranges = [(0,19), (19,34), (34, 49), (49, 63), (63, 91), (91, 106)]
divide_pdf("../Original Files/Direito_Processual_Penal.pdf", page_ranges)

def text_from_pdf_with_pdfplumber(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the text of the current page to the full text
            if page_text:
                full_text += page_text.lower() + '\n'
                full_text = re.sub(r'^alterações.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^alterado.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'pág.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'versão à data.*$', '', full_text, flags=re.MULTILINE)
                full_text = re.sub(r'^rectificado.*$', '', full_text, flags=re.MULTILINE | re.IGNORECASE)
                full_text = re.sub(r'^código penal - cp|legislação consolidada$', '', full_text, flags=re.MULTILINE)

                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    return full_text

def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

def convert_pdfs_to_txt(input_folder, output_folder):
    # Iterate over files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".pdf") and "Direito_Processual_Penal_Divided" in file:
            full_path = os.path.join(input_folder, file)
            print(full_path)
            # Extract text from PDF
            text = text_from_pdf_with_pdfplumber(full_path)
            # Define output file path (change extension from .pdf to .txt)
            output_file = os.path.join(output_folder, file)
            output_file = os.path.splitext(output_file)[0] + ".txt"
            # Write extracted text to output file
            write_to_file(text, output_file)

# Example usage:
base_dir = "../PDF Files"
output_dir = "../TXT Files"
convert_pdfs_to_txt(base_dir, output_dir)
