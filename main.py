import base64
from io import BytesIO

import cairosvg

from flask import Flask, request, jsonify

app = Flask(__name__)


def svg_to_pdf(svg_text):
  pdf_buffer = BytesIO()
  cairosvg.svg2pdf(bytestring=str(svg_text), write_to=pdf_buffer)
  pdf_buffer.seek(0)
  return base64.b64encode(pdf_buffer.read()).decode('ascii')

@app.route("/", methods=['GET'])
def convert_svg():
    try:
        svg_data = request.get_data(as_text=True)
        response = {
            "pdf": svg_to_pdf(svg_data)
        }
        status = 200
    except:
        response = {
            "message": "invalid data"
        }
        status = 400
    return jsonify(response), status
