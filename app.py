#!/usr/bin/env python3
"""Flask web application to display extracted products."""

import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from product_extractor import ProductExtractor

load_dotenv()
app = Flask(__name__)
app.secret_key = 'simple_product_extractor'

@app.route('/')
def index():
    """Display products in web interface."""
    products = load_products()
    return render_template('index.html', products=products)

@app.route('/download')
def download_json():
    """Download data.json file."""
    from flask import send_file
    if os.path.exists('data.json'):
        return send_file('data.json', as_attachment=True, download_name='products.json')
    else:
        flash('No data file found. Extract products first.', 'error')
        return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload_and_extract():
    """Upload image and extract products."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        flash('OpenAI API key not configured', 'error')
        return redirect(url_for('index'))
    
    if 'image' not in request.files:
        flash('No image file provided', 'error')
        return redirect(url_for('index'))
    
    file = request.files['image']
    if file.filename == '' or not file.filename:
        flash('No file selected', 'error')
        return redirect(url_for('index'))
    
    model = os.getenv('OPENAI_MODEL', 'gpt-4o')
    
    try:
        # Save uploaded file temporarily
        import tempfile
        file_ext = os.path.splitext(file.filename)[1].lower() or '.jpg'
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
            file.save(tmp_file.name)
            
            # Extract products
            extractor = ProductExtractor(api_key, model)
            products = extractor.extract_products(tmp_file.name)
            count = extractor.save_products(products)
            
            # Clean up temp file
            os.unlink(tmp_file.name)
            
            flash(f'Successfully extracted {count} products using {model}!', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
    
    return redirect(url_for('index'))

def load_products():
    """Load products from data.json file."""
    try:
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"Error loading products: {e}")
        return []

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)