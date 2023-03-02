#tesseract去GitHub下载

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
def read_verification_code(image_path):
    """
    Reads a verification code image and returns the text.
    """
    # Open the image file
    with Image.open(image_path) as image:
        # Convert the image to grayscale
        grayscale_image = image.convert('L')
        
        # Apply a threshold to the image to make it black and white
        threshold_image = grayscale_image.point(lambda x: 0 if x < 150 else 255)
        
        # Apply some filters to remove noise
        filtered_image = threshold_image.filter(ImageFilter.MedianFilter())
        filtered_image = filtered_image.filter(ImageFilter.MaxFilter(3))
        filtered_image = filtered_image.filter(ImageFilter.MinFilter(3))
        
        # Enhance the image to improve contrast
        contrast_enhancer = ImageEnhance.Contrast(filtered_image)
        enhanced_image = contrast_enhancer.enhance(1.5)
        
        # Use Pytesseract to extract text from the image
        pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
        text = pytesseract.image_to_string(enhanced_image)
        
        # Return the extracted text
        return text.strip()
# print(identify_verification_code("1.png"))
print(read_verification_code("1.png"))



# 从url读取

import requests
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time
def read_verification_code_from_url(url):
    # print(url)
    for i in (1,2,3,4):
        try:
            """
            Downloads an image from the given URL, reads the verification code, and returns it as text.
            """
            headers = {
            }
            # Download the image data from the URL
            response = requests.get(url,headers=headers)
            # Open the image data as a PIL Image object
            image = Image.open(BytesIO(response.content))
            # Convert the image to grayscale
            grayscale_image = image.convert('L')
            
            # Apply a threshold to the image to make it black and white
            threshold_image = grayscale_image.point(lambda x: 0 if x < 150 else 255)
            
            # Apply some filters to remove noise
            filtered_image = threshold_image.filter(ImageFilter.MedianFilter())
            filtered_image = filtered_image.filter(ImageFilter.MaxFilter(3))
            filtered_image = filtered_image.filter(ImageFilter.MinFilter(3))
            
            # Enhance the image to improve contrast
            contrast_enhancer = ImageEnhance.Contrast(filtered_image)
            enhanced_image = contrast_enhancer.enhance(1.5)
            
            # Use Pytesseract to extract text from the image
            # tessedit_char_whitelist 验证码字符集，根据实际情况修改
            config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
            pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
            text = pytesseract.image_to_string(enhanced_image,config=config)
            # 可以对长度作限制提供准确率
            return text.strip()
        
        except BaseException:
            pass
