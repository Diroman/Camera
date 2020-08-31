import json
import base64
import requests


class Sender:
    url = 'http://127.0.0.1'

    def __init__(self, url):
        self.url = url

    def send_request(self, file_name):
        headers = {'content-type': 'application/json'}
        data = open(file_name, 'rb').read()
        encoded = base64.b64encode(data)
        json_data = json.dumps(encoded.decode('ascii'))

        response = requests.post(self.url, data=json_data, headers=headers)

        return response.json()
