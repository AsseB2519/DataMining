# Import the pdfplumber library
import pdfplumber
import regex as re

# Function to extract text from each page of a PDF file
def text_from_pdf_with_pdfplumber(pdf_path):
    # Initialize an empty string to gather all the text
    full_text = ""
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through the pages of the PDF
        for page in pdf.pages[16:]:
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
                full_text = re.sub(r'^código de processo penal - cpp|legislação consolidada$', '', full_text, flags=re.MULTILINE)

                full_text = re.sub(r'\n\s*\n', '\n', full_text)
    
    # Return the full extracted text
    return full_text

# Function to write text to a file
# def write_to_file(text, output_file):

#     if pdf_path1 == 'src/Research/Código Penal.pdf':
#         output_file = "extracted_text_codigo_penal.txt"
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(text)
#     else: 
#         output_file = "extracted_text_codigo_processual_penal.txt"
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(text)

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage  
pdf_path1 = 'src/Research/Codigo_Penal.pdf'  # Path to your PDF file
pdf_path2 = 'src/Research/Codigo_Processo_Penal.pdf'  # Path to your PDF file
output_file1 = 'pdfplumber_codigo_penal.txt'  # Path to the output text file
output_file2 = 'pdfplumber_codigo_processual_penal.txt'  # Path to the output text file
extracted_text = text_from_pdf_with_pdfplumber(pdf_path1)  # Correct function name
extracted_text = text_from_pdf_with_pdfplumber(pdf_path2)  # Correct function name
write_to_file(extracted_text, output_file1)
write_to_file(extracted_text, output_file2)