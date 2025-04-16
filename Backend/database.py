from . firebase_config import db 

def AddToCollection(collection_name: str, data: dict) -> str:
    """
    Adds a document to the specified Firestore collection.
    Args:
        collection_name (str): The name of the Firestore collection.
        data (dict): The data to store in the document.
    Returns:
        str: The ID of the newly created document.
    """
    doc_ref = db.collection(collection_name).add(data)
    return doc_ref[1].id

