from . import Papi

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


@app.route("/error")
def error(request, response):
    raise Exception()


@app.route("/error2")
def error_with_message(request, response):
    raise Exception("THERE'S A FIRE!!!")


def string(request, response):
    return "this is a string"


app.add_route("/string", string)
