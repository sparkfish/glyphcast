import base64
import requests

r = requests.get("http://localhost:5000/")
json = r.json()
pdf_svg = json.get('pdf')

if pdf_svg:
    decoded = base64.b64decode(pdf_svg)
    with open("test.pdf", "wb") as f:
        f.write(decoded)


print(r, r.status_code)
