import pdfplumber
import re
import requests
from io import BytesIO
import os


def extract_watch_details_from_path(pdf_path):
    """
    Extract watch details from a PDF located at a local file path.
    """
    # Check if the file exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    
    # Open the PDF directly from the local file system
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    return extract_watch_details_from_text(text)


def extract_watch_details_from_url(pdf_url):
    """
    Extract watch details from a PDF located at a URL.
    """
    # Stream the PDF from the URL
    response = requests.get(pdf_url)
    
    # Check if the response is successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the PDF. Status code: {response.status_code}")
    
    # Open the PDF directly from the response content
    with pdfplumber.open(BytesIO(response.content)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    return extract_watch_details_from_text(text)


def extract_watch_details_from_text(text):
    """
    Extract watch details from raw text extracted from the PDF.
    """
    # Regex pattern adjusted for stricter boundary matching
    pattern = r"model\s+([\S\s]+?)\s+price\s+([\S\s]+?)(?:\n|picture)"
    matches = re.findall(pattern, text)
    
    watch_details = []
    for match in matches:
        models = match[0].split()
        prices = re.split(r'\s+(?=\$\d)', match[1])  # Split on spaces that are followed by a dollar sign and a digit

        # Clean prices to ensure they end with a dollar amount
        prices = [re.sub(r'[^\d.]+$', '', price).strip() for price in prices]

        # Match models with prices
        for i, model in enumerate(models):
            price = prices[i] if i < len(prices) else 'N/A'
            watch_details.append({"model": model, "price": price, "collection": "", "description": ""})
    
    return watch_details


def main():
    # Choose either to use a local path or a URL
    choice = input("Enter '1' for local file or '2' for URL: ").strip()
    
    if choice == '1':
        # Local file path to the PDF
        pdf_path = r'C:/Users/shayf/OneDrive/שולחן העבודה/yahavwatches/Tissot mechanical watch price list.pdf'
        watch_details = extract_watch_details_from_path(pdf_path)
    elif choice == '2':
        # URL to the PDF
        pdf_url = 'file:///C:/Users/shayf/OneDrive/%D7%A9%D7%95%D7%9C%D7%97%D7%9F%20%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94/yahavwatches/Tissot%20mechanical%20watch%20price%20list.pdf'
        watch_details = extract_watch_details_from_url(pdf_url)
    else:
        print("Invalid choice.")
        return
    
    # Display the list of dictionaries (watch details)
    print("Extracted watch details:")
    for watch in watch_details:
        print(watch)


if __name__ == "__main__":
    main()
