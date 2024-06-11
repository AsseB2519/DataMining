from fpdf import FPDF
from deep_translator import GoogleTranslator

class PDF(FPDF):
    def header(self):
        # No header
        pass

    def footer(self):
        # No footer
        pass

    def chapter_body(self, body):
        self.add_font('FreeSans', '', '../Images/FreeSans.ttf', uni=True)  # Add FreeSans font
        self.set_font('FreeSans', '', 9)  # Use FreeSans font for Unicode support
        self.set_margins(8, 8, 8)  # Smaller margins: left, top, right
        self.multi_cell(0, 5, body)  # Adjusted line height for smaller text

def text_to_pdf(text_file, pdf_file):
    pdf = PDF()
    pdf.add_page()
    
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
        translated_text = GoogleTranslator(src='pt', dest='en').translate(text)
        print(text)
        print("-" * 50)
        print(translated_text)
        # Replace double newlines with a single newline to reduce paragraph spacing
        translated_text = translated_text.replace('\n\n', '\n')
        pdf.chapter_body(translated_text)
    
    pdf.output(pdf_file)
    print(f'{pdf_file} created successfully.')

if __name__ == "__main__":
    # Example usage
    input_text_file = '../TXT Files/Caso_Pratico_CPP.txt'
    output_pdf_file = '../Final PDF Files/output.pdf'
    text_to_pdf(input_text_file, output_pdf_file)