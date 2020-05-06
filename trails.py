import requests
import json

class SecurityTrails():
    def __init__(self, args, target, handler):
        self.description = "Security Trails Module"
        self.author      = '@ahmetumitbayram'
        self.method      = ['scrape']

        self.handler     = handler
        self.target      = target


    def execute(self):
        subdomains = []
        url = "https://api.securitytrails.com/v1/domain/" + self.target + "/subdomains"
        dot = "."
        headers = {
            'accept': "application/json",
            'apikey': "YOUR_API_KEY_HERE"
        }

        response = requests.request("GET", url, headers=headers)
        list = json.loads(response.text)
        for domain in list["subdomains"]:
            subdomains.append(domain + dot + self.target)

        for sub in subdomains:
            self.handler.sub_handler({'Name': sub, 'Source': 'SecTrails'})
        return
