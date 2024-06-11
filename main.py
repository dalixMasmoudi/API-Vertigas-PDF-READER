from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
from PIL import Image
import io 
import json
import os
from datetime import datetime
from parse_data import parse_text
app = FastAPI()

def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(io.BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text



def image_to_pdf(content: bytes) -> bytes:
    image = Image.open(io.BytesIO(content))
    pdf_bytes = io.BytesIO()
    image.convert('RGB').save(pdf_bytes, format='PDF')
    return pdf_bytes.getvalue()

def save_text_to_json(filename: str, text: str) -> str:
    # Ensure the directory for storing JSON files exists
    json_dir = 'json_files'
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
    
    # Create a unique filename for the JSON file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_filename = f"{json_dir}/{filename}_{timestamp}.json"

    # Save the extracted text to the JSON file
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump({"filename": filename, "text": text}, json_file, ensure_ascii=False, indent=4)
    
    return json_filename

@app.post("/extract_text/")
async def extract_text(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".png", ".jpg", ".jpeg", ".tiff")):
        raise HTTPException(status_code=400, detail="Unsupported file type")

    content = await file.read()
    
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(content)
    else:
        pdf_content = image_to_pdf(content)
        text = extract_text_from_pdf(pdf_content)
    #structured_data = parse_text(text)
    structured_data = text
    

    json_filename = save_text_to_json(file.filename, structured_data)
  
    
    response = {
        "filename": file.filename,
        "text": text,
        "json_file": json_filename
    }
    return JSONResponse(content=response)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
