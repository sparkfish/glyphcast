import logging
import os

from glyphcast.converters import Converter, UnsupportedConversionException
from glyphcast.formats import Format
from glyphcast.utils import human_size

from flask import Flask, request, send_file
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)

MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH', None)
UPLOAD_RATE_LIMIT = os.environ.get('UPLOAD_RATE_LIMIT', "25 per minute")

if not MAX_CONTENT_LENGTH:
    logging.warn("MAX_CONTENT_LENGTH is unset, so there will be no limits on file upload size")
else:
    MAX_CONTENT_LENGTH = int(MAX_CONTENT_LENGTH)

app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

limiter = Limiter(
    app,
    key_func=get_remote_address,
)

# TODO: Add rate-limiting, configurable max file size limits
# TODO: Move the body of this method to a handler module
@limiter.limit(UPLOAD_RATE_LIMIT)
@app.route("/", methods=['PUT'])
def convert():
    if request.content_length > MAX_CONTENT_LENGTH:
        status = 413
        response = "Request too large"
        return response, status
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
        converted, converted_size = converter.convert(file_data)
        converted_size = human_size(converted_size)
        # TODO: Log the size of the converted file in bytes. This is returned
        #       when writing to the BytesIO buffer in the underlying conversion
        #       method. We might return this in future payloads that include file
        #       metadata
        logging.info(f"Converted {from_} to {to} ({converted_size=})")
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


if __name__ == '__main__':
    app.run(load_dotenv=True)
