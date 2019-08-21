import base64
import requests

import json

f = open("example.svg")

r = requests.get("https://svgtopdfservice.azurewebsites.net/", json={"svg": svg})
json = r.json()

pdf_svg = json.get('pdf')

if pdf_svg:
    decoded = base64.b64decode(pdf_svg)
    with open("test.pdf", "wb") as f:
        f.write(decoded)

f.close()
