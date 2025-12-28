# ocr_processor.py
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import os

class OCRProcessor:
    def __init__(self):
        # Tesseract path - agar installed hai toh
        try:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        except:
            pass
    
    def extract_text_from_image(self, image_file):
        """Image se product name extract kare"""
        try:
            # Open image
            if isinstance(image_file, str) and image_file.startswith('http'):
                # URL se image download kare
                response = requests.get(image_file)
                img = Image.open(BytesIO(response.content))
            else:
                # File se image open kare
                img = Image.open(image_file)
            
            # OCR process
            text = pytesseract.image_to_string(img)
            
            # Clean and extract product name
            product_name = self.clean_ocr_text(text)
            print(f"🔍 OCR Extracted: {product_name}")
            
            return product_name
            
        except Exception as e:
            print(f"❌ OCR Error: {e}")
            return "mobile phone"  # Default fallback
    
    def clean_ocr_text(self, text):
        """OCR text ko clean kare"""
        lines = text.strip().split('\n')
        
        # Remove empty lines
        lines = [line.strip() for line in lines if line.strip()]
        
        # Common OCR errors fix kare
        common_replacements = {
            'l': 'I',
            '0': 'O',
            '1': 'I',
            '5': 'S',
            'iph0ne': 'iphone',
            'samsung': 'samsung'
        }
        
        # First non-empty line (most likely product name)
        if lines:
            product_line = lines[0]
            
            # Common replacements apply kare
            for wrong, correct in common_replacements.items():
                product_line = product_line.replace(wrong, correct)
            
            return product_line
        else:
            return "electronic product"