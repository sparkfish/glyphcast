import base64
from io import BytesIO

import cairosvg

from flask import Flask, request, send_file

app = Flask(__name__)


def svg_to_pdf(svg_text):
  pdf_buffer = BytesIO()
  cairosvg.svg2pdf(bytestring=str(svg_text), write_to=pdf_buffer)
  pdf_buffer.seek(0)
  return pdf_buffer

@app.route("/", methods=['GET'])
def convert_svg():
    try:
        svg_data = request.get_data(as_text=True)
        svg_pdf = svg_to_pdf(svg_data)
        response = send_file(svg_pdf, attachment_filename='svg.pdf', mimetype='application/pdf')
        status = 200
    except:
        response = "invalid data"
        status = 400
    return response, status
