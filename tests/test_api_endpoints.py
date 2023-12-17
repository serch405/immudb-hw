from config import url_collection, url_collections, url_document, private_key
from endpoints.collection import Collection
from endpoints.collections import Collections
from endpoints.document import Document


def test_document_creation():

    # remove all exesting collections
    response = Collections("get", url_collections, private_key)
    for collection in response.get_all_names():
        Collection("delete", url_collection, collection, private_key)

    # create a new collection with "test-collection" name
    Collection("put", url_collection, "test-collection", private_key)
    
    # print details of just created collection
    print(Collection("get", url_collection, "test-collection", private_key).get_json())

    # create a new document with "test-document" name inside the collection
    response = Document("put", url_document, "test-document", private_key)
    assert response.get_status() == 200
