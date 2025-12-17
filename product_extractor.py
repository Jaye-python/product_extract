"""Core product extraction logic using OpenAI Vision API."""

import json
from openai import OpenAI
from file_upload import preprocess_image

class ProductExtractor:
    def __init__(self, api_key, model="gpt-4o"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
    
    def extract_products(self, image_path):
        """Extract products from leaflet image."""
        base64_image = preprocess_image(image_path)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Analyze product leaflet images and extract all products. Return ONLY a JSON array with this exact structure: [{\"name\": \"product name\", \"price\": \"price\", \"description\": \"description\"}]. Do not include any other text."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ]
        )
        
        content = response.choices[0].message.content
        if content is None or content.strip() == "":
            raise ValueError("OpenAI returned empty response")
        
        # Clean the response - sometimes it has markdown formatting
        content = content.strip()
        if content.startswith('```json'):
            content = content[7:]
        if content.endswith('```'):
            content = content[:-3]
        content = content.strip()
        
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response from OpenAI: {content[:200]}...") from e
    
    def save_products(self, products, filename='data.json'):
        """Save products to JSON file."""
        with open(filename, 'w') as f:
            json.dump(products, f, indent=2)
        return len(products)