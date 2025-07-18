import os
from pdf2image import convert_from_path
from typing import Optional

# Define paths
pdf_file = os.path.join('Data', 'Input_pdf_folder')
output_folder = os.path.join('Data', 'Images')
Poppler_path = r'C:\Program Files\poppler-24.08.0\Library\bin'

# Function to convert PDF to images
def convert_pdf_to_image(pdf_filename: str, poppler_path: Optional[str] = None) -> str:
    # Full path to the input PDF file
    pdf_path = os.path.join(pdf_file, pdf_filename)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Convert PDF to image list
    images = convert_from_path(pdf_path, poppler_path=Poppler_path)
    
    # Save each image as a separate PNG file
    for i, image in enumerate(images):
        filename = os.path.join(output_folder, f"image_{i+1}.png")
        image.save(filename, 'PNG')
    
    # Return the output folder path
    print(f"pdf file uploaded successfully")
    return output_folder

if __name__=="__main__":
    convert_pdf_to_image("given_pdf", poppler_path=Poppler_path)


