import os

def search_watch_by_model(db, model_name):
    """
    Search the Watches collection for a document with the given model name
    and return the supplier information.
    """
    # Reference the Watches collection
    watches_ref = db.collection('Watches')
    
    # Query for watches with the specified model
    query = watches_ref.where('model', '==', model_name).stream()
    
    # Iterate over the results
    for watch in query:
        watch_data = watch.to_dict()
        supplier = watch_data.get('supplier', 'Unknown Supplier')
        print(f"Model: {model_name}")
        print(f"Supplier: {supplier}")
        return supplier
    
    print(f"No watch found with model: {model_name}")
    return None


def upload_pdf_to_storage(bucket, pdf_file, pdf_name):
    """
    Uploads a PDF to Firebase Storage from an uploaded file and returns the URL.
    """
    blob = bucket.blob(f"catalog_pdfs/{pdf_name}")  # Path in the bucket where the PDF will be stored
    blob.upload_from_file(pdf_file)

    # Make the file publicly accessible
    blob.make_public()

    # Return the public URL of the uploaded PDF
    return blob.public_url

def add_catalog_entry(db, title, description, pdf_url):
    """
    Adds a new document to the 'catalog' collection in Firestore.
    """
    catalog_ref = db.collection('catalog')
    new_entry = {
        'title': title,
        'description': description,
        'pdf_url': pdf_url
    }

    # Add the document to Firestore
    catalog_ref.add(new_entry)
    print(f"Document added to 'catalog' collection with title: {title}")

def compare_and_find_new_watches(db, new_watches):

    # Fetch existing watches from Firestore
    watches_ref = db.collection('Watches')
    existing_watches = watches_ref.stream()

    # Convert existing watches to a set of (model, price) tuples for faster lookup
    existing_watch_set = set(
        (watch.to_dict().get('model')) for watch in existing_watches
    )

    # Find new watches that are not in the existing watch set
    new_unique_watches = [
        watch for watch in new_watches 
        if (watch['model']) not in existing_watch_set
    ]

    return new_unique_watches
def add_new_watches(db, watches,):

    # Reference to the 'Watches' collection
    watches_ref = db.collection('Watches')

    # Loop through each watch in the list and add it to Firestore
    for watch in watches:
        watches_ref.add(watch)
        print(f"New watch added with model: {watch['model']}")
