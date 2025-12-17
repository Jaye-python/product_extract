# Product Data Extraction Pipeline

A Python application that extracts product information from leaflet images using OpenAI's Vision API and displays results in a web interface.

## Features

- Extract product data from JPG/PNG leaflet images
- Generate structured JSON output
- Web interface with clickable product table
- Automatic image preprocessing and optimization

## Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure OpenAI API:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key and model
   ```

## Usage

**Run the web application:**

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser to:
- Upload leaflet images directly
- View extracted products in a table
- Click rows to select and view details

**Alternative - Command line:**

```bash
python main.py
```

Enter the path to your leaflet image when prompted.

## Technology Choices

- **OpenAI GPT-4V**: Best accuracy for structured data extraction from images
- **Direct API calls**: Simpler than frameworks, fewer dependencies
- **Flask**: Lightweight web framework for quick setup
- **Pillow**: Image preprocessing and optimization
- **No OCR libraries**: Vision model handles text recognition internally

## Output Format

Products are extracted in this JSON structure:
```json
[
  {
    "name": "Product Name",
    "price": "Price",
    "description": "Description"
  }
]
```

## Limitations

- Requires OpenAI API key and credits
- Accuracy depends on image quality and layout
- Limited to 2048px max image size
- Text-heavy leaflets work best

## Improvements

- Add batch processing for multiple images
- Implement confidence scoring
- Add product image extraction
- Support for more output formats
- Enhanced error handling and validation

## Project Structure

```
product_extract/
├── main.py              # Main extraction script
├── app.py               # Flask web application
├── product_extractor.py # Core extraction logic
├── file_upload.py       # Image processing utilities
├── requirements.txt     # Dependencies
├── data.json           # Output JSON file (generated)
├── templates/
│   └── index.html      # Web interface template
├── static/
│   └── style.css       # Basic styling
├── .env.example        # Environment variables template
└── README.md           # This documentation
```

## Modular Architecture

- **file_upload.py**: Image validation and preprocessing utilities
- **product_extractor.py**: Core OpenAI Vision API integration  
- **main.py**: Command-line interface
- **app.py**: Simple web interface with form handling