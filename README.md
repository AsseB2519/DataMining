# DataMining - LawTalk Project

The LawTalk Project consists of developing a chatbot using Ollama LLM's and the integration of RAG to create a chatbot that analyses and answers practical cases regarding crimes utilizing the Portuguese Penal Code and the Portuguese Processual Penal Code.

## Team Members

- **PG50380** - Francisco Claudino
- **PG50633** - Mariana Marques
- **PG53597** - Afonso Bessa
- **PG54780** - Eduardo Henriques

## Index of Contents

### `src`: Contains the Source Code of the Project

- **`app.py`**: Contains the core chatbot implementation using Ollama LLM's.
- **`divide_pdf.py`**: Contains the script to divide PDF files in many smaller PDF's.
- **`document_loader.py`**: Contains the script for loading the PDF files to the database.
- **`evaluate.csv`**: Contains the Test Dataset for the evaluation of the LLM Models.
- **`evaluate.py`**: Contains the Jupyter Notebook for evaluating the LLM Models.
- **`streamlit.py`**: Main script to run the chatbot.
- **`llm.py`**: Contains the prompts and the chain build with the RAG Framework.
- **`models.py`**: Contains code that verifies and downloads the LLM Models if not present in the local machine.
- **`extract_pdfplumber.py`**: Contains the code for extracting raw text from PDF files using PDFPlumber.
- **`py2pdf.py`**: Contains the code for extracting raw text from PDF files using Py2PDF.
- **`tesseract.py`**: Contains the code for extracting raw text from PDF files using Tesseract.
- **`requirements.txt`**: Contains the tools necessary to run the project.

#### `docs`: Contains both presentations and the report.

#### `Original Files`: Contains the original PDF files for the Portuguese Penal and Processual Penal Code.

#### `TXT Files`: Contains the files in TXT format extracted from the Original Files.

#### `Images`: Contains the images used in the web application of the project.

#### `Codigo_Penal_Divided`: Contains the Portuguese Penal Code divided in variou PDF files.

#### `Embeddings`: Contains the vector embeddings of the LLM Models.
