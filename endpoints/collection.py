import requests
import json
from endpoints.base import Base


class Collection(Base):

    def __init__(self, request_type, url, collection, private_key):
        formatted_url = url.format(collection=collection)
        headers = {
            "accept": "application/json",
            "X-API-Key": private_key,
            "Content-Type": "application/json"
        }

        if request_type == 'put':
            data = {
                "idFieldName": "account_number",
                "fields": [
                    {"name": "account_name"},
                    {"name": "iban"},
                    {"name": "address"},
                    {"name": "amount"},
                    {"name": "type"}
                ],
                "indexes": []
            }
            self.response = requests.put(formatted_url, headers=headers, data=json.dumps(data))

        elif request_type == 'get':
            self.response = requests.get(formatted_url, headers=headers)

        elif request_type == 'delete':
            self.response = requests.delete(formatted_url, headers=headers)

        elif request_type == 'post':
            raise ValueError(f"Under development request type: {request_type}")

        else:
            raise ValueError(f"Unsupported request type: {request_type}")
