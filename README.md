# SVG to PDF Service

This is a small service that converts SVG payloads into PDF bytes. The server response to a valid payload is the raw binary PDF. If you save the response to a file, it should load in a PDF viewer with no additional processing. Clients can determine success or failure by the HTTP status code returned.

See [client.py](https://github.com/team-sparkfish/svg-to-pdf-service/blob/master/client.py) for example client usage, or use the example JSON payload:

**HTTPie**

``` shell
http -d GET https://svgtopdfservice.azurewebsites.net/ @sparkfish.svg --output sparkfish.pdf
```


**cURL**

``` shell
curl -vX GET https://svgtopdfservice.azurewebsites.net/ -d @sparkfish.svg --header "Content-Type: application/text" > sparkfish.pdf
```

# Development

To install dependencies, `pip install -r requirements.txt`
Run with gunicorn `gunicorn --workers=4 main:app` 

# Deployment

On push to master, a Docker image is built and pushed to a container registry via Azure DevOps to a continuously deployed Linux Container App at https://svgtopdfservice.azurewebsites.net/.

# Roadmap

- [ ] Authorization (API keys/bearer tokens) 
- [ ] More robust status codes 
