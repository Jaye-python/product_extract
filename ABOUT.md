# About Product Data Extraction Pipeline

## Overview
A Python web application that extracts product information from leaflet images using OpenAI's Vision API and displays results in an interactive table with download functionality.

## Key Features
- **Image Upload**: Direct browser upload of JPG/PNG leaflet images
- **AI Extraction**: Uses OpenAI Vision models to extract product data
- **Interactive Table**: Clickable rows for product selection
- **JSON Download**: Export extracted data as downloadable JSON file
- **Modular Design**: Clean separation of concerns across modules

## Technology Stack
- **Backend**: Python, Flask
- **AI**: OpenAI Vision API (GPT-4o/GPT-5-nano)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Pillow (PIL)
- **Environment**: python-dotenv

## Use Cases
- Retail inventory management
- Product catalog digitization
- Price comparison analysis
- Market research data collection
- E-commerce product listing automation

## Quick Start
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure OpenAI API key in `.env`
4. Run: `python app.py`
5. Upload leaflet image at `http://127.0.0.1:5000`

## Output Format
Extracts products as JSON with name, price, and description fields for easy integration with existing systems.