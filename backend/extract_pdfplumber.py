# Import the pdfplumber library
import pdfplumber

# Function to extract text from each page of a PDF file
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
                full_text += page_text + '\n'
    
    # Return the full extracted text
    return full_text

# Function to write text to a file
def write_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
pdf_path = r'src\Leis\Código Penal.pdf'  # Path to your PDF file
output_file = 'extracted_text_pdfplumber.txt'  # Path to the output text file
extracted_text = text_from_pdf_with_pdfplumber(pdf_path)  # Correct function name
write_to_file(extracted_text, output_file)
