import pytesseract as pyt
from PIL import ImageEnhance, ImageFilter, Image
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io


def extract_images_from_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    images = []
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        
        # Extract images from the page
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)
    
    pdf_document.close()
    return images

def ocr_image(image):
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf_images(pdf_path):
    images = extract_images_from_pdf(pdf_path)
    texts = [ocr_image(image) for image in images]
    return texts

# Example usage
pdf_path = 'image_2.pdf'  # Path to your PDF file
texts = extract_text_from_pdf_images(pdf_path)

# Print the extracted text from each image
for i, text in enumerate(texts):
    print(f"Text from image {i + 1}:\n{text}\n")