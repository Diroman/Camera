import requests


class Sender:
    url = 'http://127.0.0.1'

    def __init__(self, url):
        self.url = url

    def send_request(self, data):
        headers = {'content-type': 'application/json'}
        response = requests.post(self.url, data=data, headers=headers)

        return response.json()
