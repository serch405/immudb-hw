import requests
import json
from endpoints.base import Base


class Collections(Base):

    def __init__(self, request_type, url, private_key):
        headers = {
            "accept": "application/json",
            "X-API-Key": private_key,
            "Content-Type": "application/json"
        }

        if request_type == 'get':
            self.response = requests.get(url, headers=headers)
        
        else:
            raise ValueError(f"Unsupported request type: {request_type}")

    def get_all_names(self):
        return [collection['name'] for collection in self.get_json()['collections']]
