import base64
import requests

import json

with open("sparkfish.svg") as f:
    svg = f.read()

r = requests.get("https://svgtopdfservice.azurewebsites.net", data=svg)

json = r.json()
pdf_svg = json.get('pdf')

if pdf_svg:
    decoded = base64.b64decode(pdf_svg)
    with open("sparkfish.pdf", "wb") as f:
        f.write(decoded)
else:
    print("Request invalid")
    
f.close()
