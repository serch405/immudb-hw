import configparser
import os


config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

url_collection = config.get("URLS", "URL_COLLECTION")
url_collections = config.get("URLS", "URL_COLLECTIONS")
url_document = config.get("URLS", "URL_DOCUMENT")

private_key = config.get("KEYS", "PRIVATE_KEY")
public_key = config.get("KEYS", "PUBLIC_KEY")
