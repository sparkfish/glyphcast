# SVG to PNG Service

This is a small service that compiles SVG payloads into a base64-encoded string. See [client.py](https://github.com/team-sparkfish/svg-to-pdf-service/blob/master/client.py) for example client usage, or use the example JSON payload:

**HTTPie**

``` shell
http https://svgtopdfservice.azurewebsites.net/ < sparkfish.svg
```


**cURL**

``` shell
curl -vX GET https://svgtopdfservice.azurewebsites.net/ -d @sparkfish.svg --header "Content-Type: application/svg"
```


# Development

To install dependencies, `pip install -r requirements.txt`
Run with gunicorn `gunicorn --workers=4 main:app` 

# Deployment

On push to master, a Docker image is built and pushed to a container registry via Azure DevOps to a continuously deployed cLinux Container App at https://svgtopdfservice.azurewebsites.net/.
