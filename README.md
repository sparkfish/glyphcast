# Glyphcast

Glyphcast casts your DOCX and SVG files into beautiful PDFs. 

See [client.py](https://github.com/team-sparkfish/svg-to-pdf-service/blob/master/client.py) for example client usage, or use the example SVG payload:

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
