# SVG to PNG Service

This is a small service that compiles SVG payloads into a base64-encoded string. See [client.py](https://github.com/team-sparkfish/svg-to-pdf-service/blob/master/client.py) for an example request.

# Development

To install dependencies, `pip install -r requirements.txt`
Run with gunicorn `gunicorn --workers=4 main:app` 

# Deployment

On push to master, a Docker image is built and pushed to a container registry via Azure DevOps to a continuously deployed cLinux Container App at https://svgtopdfservice.azurewebsites.net/.
