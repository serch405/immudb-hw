import requests
import json


class Base:

    def get_status(self):
        return self.response.status_code

    def get_json(self):
        return self.response.json()
