import base64
import requests

from io import BytesIO

with open("sparkfish.svg") as f:
    svg = f.read()

r = requests.get("http://localhost:5000", data=svg)

pdf_svg = r.content

if pdf_svg:
    with open("sparkfish.pdf", "wb") as f:
        f.write(pdf_svg)
else:
    print("Request invalid")
    
f.close()
