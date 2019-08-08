# Papi

A small API focused web framework. Based off the ideas of [Flask](https://palletsprojects.com/p/flask/) and [Hapi](https://hapi.dev/)

```
from papi import Papi

app = Papi()

@app.route("/")
def home(request, response):
    return {"status": "Successful", "message": "Hello from the home page."}


@app.route("/hello")
def hello(request, response):
    name = request.params.get("name", "World")
    return {"status": "Successful", "message": f"Hello, {name}!"}


@app.route("/count")
@app.route("/count/{num}")
def count(request, response, num=0):
    return f"The count is {num}."


def string(request, response):
    return "this is a string"


app.add_route("/string", string)
```

Uses [webob](https://webob.org/) and [guincorn](https://gunicorn.org/) to function. Started from following [this amazing blog post](http://rahmonov.me/posts/write-python-framework-part-one/).

## Development

```
$ pipenv shell
$ pipenv install
$ gunicorn papi.app:app --reload
```
