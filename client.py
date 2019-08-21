import base64
import requests

import json

with open("sparkfish.svg") as f:
    svg = f.read()

print(svg)
r = requests.get("http://localhost:5000/", data=svg)

json = r.json()
pdf_svg = json.get('pdf')

if pdf_svg:
    decoded = base64.b64decode(pdf_svg)
    with open("sparkfish.pdf", "wb") as f:
        f.write(decoded)
else:
    print("Request invalid")
    
f.close()
