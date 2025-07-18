import os
from typing import Optional
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Input images folder
Image_folder = os.path.join('Data', 'Images')

# Output file inside the 'Extracted_texts' folder
Output_folder = os.path.join('Data', 'Extracted_texts')
Output_text_file = os.path.join(Output_folder, 'output.txt')  

def run_ocr_on_images(image_folder: str = Image_folder, output_file_path: str = Output_text_file) -> Optional[str]:
    # Ensure the output folder exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Get all image files (png, jpg, jpeg)
    image_files = sorted([
        f for f in os.listdir(image_folder)
        if f.lower().endswith(('.png', 'jpg', 'jpeg'))
    ])

    if not image_files:
        print("No images found in:", image_folder)
        return None

    print("Number of images found:", len(image_files))

    # Write extracted text to a single output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for filename in image_files:
            image_path = os.path.join(image_folder, filename)

            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            text = pytesseract.image_to_string(thresh)

            output_file.write(f"\n-- Page: {filename} --\n")
            output_file.write(text)
            output_file.write("\n")

    print("OCR completed successfully.")
    return output_file_path

# Run directly
if __name__ == "__main__":
    run_ocr_on_images()
