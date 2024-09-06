from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
app = FastAPI()

@app.post("/extract-text/")
def extract_text(image_file: UploadFile = File(...)):
    image = Image.open(image_file.file)
    text = pytesseract.image_to_string(image)
    return {"extracted_text": text}

