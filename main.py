import logging

from glyphcast.converters import Converter, UnsupportedConversionException
from glyphcast.formats import Format

from flask import Flask, request, send_file

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)

# TODO: Add rate-limiting, configurable max file size limits
# TODO: Move the body of this method to a handler module
@app.route("/", methods=['PUT'])
def convert():
    # Determine source/to conversion formats, possibly from filename extension or querystring
    # Attempt to perform the conversion
    # If conversion fails, return a 400 if due to unsupported format or malformed data
    # If conversion fails due to something else, return a 500 error
    from_ = request.args.get("from", "")
    to = request.args.get("to", "")
    file_data = request.data
    conversion_type = Converter.conversion_type(from_, to)
    logging.info(f"Received query with conversion type {conversion_type}")
    converter = Converter(*conversion_type)
    try:
        converted = converter.convert(file_data)
        # TODO: Log the size of the converted file in bytes. This is returned
        #       when writing to the BytesIO buffer in the underlying conversion
        #       method. We might return this in future payloads that include file
        #       metadata
        logging.info(f"Converted {from_} to {to}")
        # Only PDF responses are supported currently
        # When more responses are supported the converter
        # object can be augmented to determine the correct mimetype to return
        # Flask.send_file can guess mimetype based on the filename
        response = send_file(
          converted,
          attachment_filename='document.pdf',
          mimetype='application/pdf',
          as_attachment=True
        )
        status = 200

    except UnsupportedConversionException as e:
        status = 415
        response = e.args[0]
        logging.warn(f"{response}")
    except Exception as unhandled:
        status = 500
        response = f"Something went wrong on our end"
        logging.error(f"Encountered an unhandled exception: {unhandled}")
    logging.info(f"Responding with status code {status}: {response}")
    return response, status
