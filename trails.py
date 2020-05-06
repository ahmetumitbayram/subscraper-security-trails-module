import requests
import json

class SecurityTrails():
    def __init__(self, args, target, handler):
        self.description = "Example module"
        self.author      = '@m8r0wn'
        self.method      = ['scrape']

        self.handler     = handler
        self.target      = target


    def execute(self):
        subdomains = []
        url = "https://api.securitytrails.com/v1/domain/" + self.target + "/subdomains"
        dot = "."
        headers = {
            'accept': "application/json",
            'apikey': "njuX3LKA5D3SoKJzg8yZDIxDo2h8mlZg"
        }

        response = requests.request("GET", url, headers=headers)
        list = json.loads(response.text)
        for domain in list["subdomains"]:
            subdomains.append(domain + dot + self.target)

        for sub in subdomains:
            self.handler.sub_handler({'Name': sub, 'Source': 'SecTrails'})
        return
