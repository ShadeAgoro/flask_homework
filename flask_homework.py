from flask import Flask, Response, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def say_hello_page(name):
    return """
<html>
<head>
    <title> Sample - Flask routes</title>
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
</body>
</html>
""".format(name)
# triple quote marks displays data over multiple lines


@app.route('/about/page')
def about_page():
     return Response ("This is the about page", mimetype='text/plain')

@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')
@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
    <title style="color:coral ; ">Sample - Flask routes</title>
</head>

<body>
    <h1 style="color:coral ;">Welcome to our Website</h1>
    <p>Hello {}!</p>
    <p>You are {} year(s) old.</p>
    <hr>
    <h2 style="color: coral;"> Why Use Flask</h2>
    <p>Flask is a web application framework written in Python.It was developed by Armin Ronacher, who led a team of 
    international Python enthusiasts called Pooco. Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template 
    engine. Both are Pocco projects. </p> 
    <br>
    <a href= "{}">Welcome</a>
</body>
</html>
""".format(name, age, url)


if __name__ == "__main__":
    app.run(debug=True)
