import requests
import json
from endpoints.base import Base


class Document(Base):

    def __init__(self, request_type, url, collection, private_key):
        formatted_url = url.format(collection=collection)
        headers = {
            "accept": "application/json",
            "X-API-Key": private_key,
            "Content-Type": "application/json"
        }

        if request_type == 'put':
            data = {
                "account_number": "my account number",
                "account_name": "my account name",
                "iban": "my iban",
                "address": "my address",
                "amount": "my amount",
                "type": "sending"
            }

            self.response = requests.put(formatted_url, headers=headers, data=json.dumps(data))

        elif request_type == 'post':
            raise ValueError(f"Under development request type: {request_type}")

        else:
            raise ValueError(f"Unsupported request type: {request_type}")
