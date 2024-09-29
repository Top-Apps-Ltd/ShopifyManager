from flask import Flask,jsonify,request
from db import Firestore
from services import neworderemail
from services import FirestoreService
from services import extractor
from services import chatgptcollection



app = Flask(__name__)
db, bucket = Firestore.initialize_firebase()

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """
    Route to upload a PDF and add an entry to the Firestore 'catalog' collection.
    """
    # Get JSON data (title and description)
    json_data = request.get_json()
    
    # Validate JSON data
    if not json_data or 'title' not in json_data or 'description' not in json_data:
        return jsonify({"error": "JSON body must include 'title' and 'description'"}), 400
    
    title = json_data['title']
    supplieremail = json_data['supplieremail']

    # Check if the request contains a file part
    if 'pdf' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    # Get the file from the request
    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Optional: Validate file type
    if not pdf_file.filename.endswith('.pdf'):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    # Generate a unique filename for the PDF to avoid overwriting
    pdf_name = pdf_file.filename

    # Upload the PDF to Firebase Storage
    try:
        pdf_url = FirestoreService.upload_pdf_to_storage(bucket, pdf_file, pdf_name)
        print(f"PDF uploaded to: {pdf_url}")
    except Exception as e:
        return jsonify({"error": f"Failed to upload PDF: {str(e)}"}), 500

    # Add the catalog entry to Firestore
    try:
        FirestoreService.add_catalog_entry(db, title, supplieremail, pdf_url)
    except Exception as e:
        return jsonify({"error": f"Failed to add catalog entry: {str(e)}"}), 500

    # Return success response
    Watches = extractor.extract_watch_details_from_url(pdf_url)
    NewWatches = FirestoreService.compare_and_find_new_watches(Watches)
    WatchesWithDescription = chatgptcollection.enrich_watch_details_with_chatgpt(NewWatches,supplieremail)
    FirestoreService.add_new_watches(WatchesWithDescription)



    return jsonify({"message": "PDF uploaded and catalog entry added successfully", "pdf_url": pdf_url}), 200




@app.route('/neworder')




@app.route('/newcatalog')
def neworder(Watches):
    data = {
            'Watches': Watches,
        }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
    