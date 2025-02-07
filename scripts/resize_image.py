from PIL import Image
import os
import xml.etree.ElementTree as ET


def resize_image(image_filename, max_height=120):
    """
    Resize an image to a maximum height, keeping the aspect ratio.
    The image is resized in place.
    param image_filename: The image file to resize
    param max_height: The maximum height in pixels
    TODO: Add support for other image formats
    """
    if os.path.exists(image_filename):
        with Image.open(image_filename) as img:
            width, height = img.size
            if height > max_height:
                new_height = max_height
                new_width = int((new_height / height) * width)

                img_resized = img.resize(
                    (new_width, new_height), Image.LANCZOS
                )

                # Determine the file format
                file_format = image_filename.split('.')[-1].upper()
                if file_format == 'JPG':
                    file_format = 'JPEG'

                # Save the resized image with optimization
                img_resized.save(
                    image_filename,
                    format=file_format,
                    optimize=True,
                    quality=85
                )
    else:
        print(f'File not found: {image_filename}')

# Transform an image into webp format
def convert_to_webp(image_filename, replace=False):
    """
    Convert an image to webp format.
    The image is converted in place.
    param image_filename: The image file to convert
    """
    supported_formats = ['.png', '.jpg', '.jpeg', '.tiff']
    image_ext = os.path.splitext(image_filename)[1].lower()
    if image_ext not in supported_formats:
        return image_filename
    if os.path.exists(image_filename):
        with Image.open(image_filename) as img:
            # Determine the file format
            file_format = image_filename.split('.')[-1].upper()

            # Save the image in webp format with optimization
            webp_filename = image_filename.replace(file_format.lower(), 'webp')
            img.save(
                webp_filename,
                format='WEBP',
                optimize=True,
                quality=85
            )
            if replace:
                os.remove(image_filename)
        return webp_filename
    else:
        print(f'File not found: {image_filename}')
        raise FileNotFoundError
    
# Check if the image is valid
def is_valid_image(image_filename):
    """
    Check if the image file is valid.
    param image_filename: The image file to check
    return: True if the image is valid, False otherwise
    """
    try:
        img = Image.open(image_filename)
        img.verify()
        return True
    except Exception as e:
        print(f'Invalid image: {image_filename}')

def is_valid_svg(svg_filename):
    """
    Check if the svg file is valid.
    param svg_filename: The svg file to check
    return: True if the svg is valid, False otherwise
    """
    try:
        ET.parse(svg_filename)  # Try to parse the XML
        return True  # No error means it's valid
    except ET.ParseError:
        return False  # If parsing fails, it's invalid