import base64
from io import BytesIO

import cairosvg

from flask import Flask, request, jsonify

app = Flask(__name__)

test_svg = """
<svg height="400" width="450">
<path id="lineAB" d="M 100 350 l 150 -300" stroke="red" stroke-width="3" fill="none" />
  <path id="lineBC" d="M 250 50 l 150 300" stroke="red" stroke-width="3" fill="none" />
  <path d="M 175 200 l 150 0" stroke="green" stroke-width="3" fill="none" />
  <path d="M 100 350 q 150 -300 300 0" stroke="blue" stroke-width="5" fill="none" />
  <!-- Mark relevant points -->
  <g stroke="black" stroke-width="3" fill="black">
    <circle id="pointA" cx="100" cy="350" r="3" />
    <circle id="pointB" cx="250" cy="50" r="3" />
    <circle id="pointC" cx="400" cy="350" r="3" />
  </g>
  <!-- Label the points -->
  <g font-size="30" font-family="sans-serif" fill="black" stroke="none" text-anchor="middle">
    <text x="100" y="350" dx="-30">A</text>
    <text x="250" y="50" dy="-10">B</text>
    <text x="400" y="350" dx="30">C</text>
  </g> 
  Sorry, your browser does not support inline SVG. 
</svg>
"""

def svg_to_pdf(svg_text=test_svg):
  pdf_buffer = BytesIO()
  cairosvg.svg2pdf(bytestring=str(svg_text), write_to=pdf_buffer)
  pdf_buffer.seek(0)
  return base64.b64encode(pdf_buffer.read()).decode('ascii')

@app.route("/", methods=['GET'])
def convert_svg():
    try:
        #svg_data = request.json.get('svg')
        response = {
            "pdf": svg_to_pdf()
        }
        status = 200
    except:
        response = {
            "message": "invalid data"
        }
        status = 400
    return jsonify(response), status

if __name__ == '__main__':
    app.run(debug=True)
