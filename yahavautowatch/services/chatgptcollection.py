import openai
import re

def enrich_watch_details_with_chatgpt(watches,supplieremail):
    for watch in watches:
        # Frame the question to request specific information about the watch model
        query = f"Provide the collection name and a concise description suitable for an online store for the watch model {watch['model']}."
        messages = [
            {"role": "system", "content": "You are an assistant knowledgeable about watch models."},
            {"role": "user", "content": query}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=250,
                stop=None,
                temperature=0.5
            )

            # Extract the text from the response
            text = response.choices[0].message['content'].strip()

            # Use regex to parse 'collection' and 'description' from the text
            collection_match = re.search(r"Collection Name: ([^\.\n]+)", text)  # Adjusted regex to stop at the first period or newline
            description_match = re.search(r"Description: (.+)", text)

            # Update the watch dictionary based on parsed data
            watch['collection'] = collection_match.group(1).strip() if collection_match else "Collection information unavailable"
            watch['description'] = description_match.group(1).strip() if description_match else "No detailed description available"
            watch['supplieremail'] = supplieremail
        except Exception as e:
            print(f"Error querying model {watch['model']}: {e}")
            watch['collection'] = "Error retrieving collection information"
            watch['description'] = "Error retrieving description"

    return watches

# Example usage with the watches list initialized with model and price
watches = [
{'model': 'T120.407.17.041.01', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T120.407.17.051.00', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T120.407.17.041.00', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T120.407.37.051.00', 'price': '$383.00', 'collection': '', 'description': ''},
{'model': 'T120.407.17.041.00', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T122.407.22.031.00', 'price': '$383.00', 'collection': '', 'description': ''},
{'model': 'T122.407.11.031.00', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T122.407.11.051.00', 'price': '$373.00', 'collection': '', 'description': ''},
{'model': 'T120.407.11.041.02', 'price': '$373.00', 'collection': '', 'description': ''}
]

# Assuming your API key is set and correct
openai.api_key = 'sk-proj-DunmLrC2PZXFgGLODtfQT3BlbkFJFpv71rGDfSj3R1eUEaBs'
enriched_watches = enrich_watch_details_with_chatgpt(watches,"shayfarah3475@gmail.com")
print(enriched_watches)
