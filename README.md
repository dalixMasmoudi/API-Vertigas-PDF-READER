# VESTIGAS OCR PoC Coding Challenge

## Introduction
This project provides a FastAPI application to demonstrate the extracting text information from images or PDFs using OCR.
NOTE: CURRENTLY THIS ONLY WORKS WELL WITH PDFS. YOU CAN UPLOAD IMAGES BUT IT WILL PROBABLY WONT DELIVER ANY TEXT.



## Installation
1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install requirements.txt
   ```
## Usage
1. Run the FastAPI application:
```bash
    uvicorn main:app --reload
```
2.Use a tool like curl or Postman to test the endpoint:
```bash
    curl -X POST "http://127.0.0.1:8000/extract_text/" -F "file=@path_to_your_file"
```
## API Endpoint
1.POST /extract_text/
        Description: Receives an image or PDF file and returns the recognized text as JSON.
        Request Body: Multipart/form-data with the file.
        Response: JSON object containing the filename and extracted text. JSON file is going to be saved on json_files folder.