from flask import Flask


app= Flask(__name__)
@app.route("/")
def index():
    return("Hello World!")

@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/<grade>/<name>")
def ooh(grade, name):
    return f"Hello {name} from {grade}."

app.run(debug=True)