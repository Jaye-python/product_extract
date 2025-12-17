# product_extract/file_upload.py
"""Image processing utilities for product extraction."""

import os
import base64
import io
from PIL import Image

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}
MAX_IMAGE_SIZE = 2048


def validate_image_file(image_path):
    """Validate image file exists and has correct extension."""
    if not os.path.exists(image_path):
        raise ValueError(f"Image file not found: {image_path}")
    
    file_ext = os.path.splitext(image_path)[1].lower()
    if file_ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValueError(f"Unsupported image format. Allowed: {', '.join(ALLOWED_IMAGE_EXTENSIONS)}")
    
    return True

def preprocess_image(image_path):
    """Load and preprocess image for OpenAI API."""
    validate_image_file(image_path)
    
    with Image.open(image_path) as img:
        # Resize if too large
        if max(img.size) > MAX_IMAGE_SIZE:
            img.thumbnail((MAX_IMAGE_SIZE, MAX_IMAGE_SIZE), Image.Resampling.LANCZOS)
        
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Convert to base64
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=85)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
