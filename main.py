#!/usr/bin/env python3
"""Product extraction from leaflet images using OpenAI Vision API."""

import os
from dotenv import load_dotenv
from product_extractor import ProductExtractor

load_dotenv()

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Create a .env file with: OPENAI_API_KEY=your_key_here")
        return
    
    model = os.getenv('OPENAI_MODEL', 'gpt-4o')
    image_path = input("Enter path to leaflet image: ").strip()
    
    try:
        extractor = ProductExtractor(api_key, model)
        products = extractor.extract_products(image_path)
        count = extractor.save_products(products)
        
        print(f"Extracted {count} products using {model} and saved to data.json")
        
        if products:
            print("\nExtracted products:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product['name']} - {product['price']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()