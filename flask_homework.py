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

@app.route('/about/page')
def about_page():
     return Response("This is the about page", mimetype='text/plain')

@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/html')
@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    image = url_for('static', filename='flask.jpg')
    return """

<html>
<head>
    <title>Sample - Flask routes</title>
</head>

<body>
    <h1 style="color:aqua ;">Welcome to our Website</h1>
    <p>Hello {}!</p>
    <p>You are {} year(s) old.</p>
    <hr>
    <h2 style="color: aqua;"> Why Use Flask</h2>
    <img src="{}" height='300' width='300' alt="Image of Python Flask">
    <p>A flask is a small container that holds a liquid. Most flasks have a squarish body and a small neck for 
    drinking or pouring. Don't try sneaking a flask into your tube sock.There are several different kinds of flasks, 
    including a "hip flask," small enough to fit in a pocket, for carrying and surreptitiously sipping alcoholic 
    beverages. Chemists use another type of flask in the laboratory, which has a wide bottom and a small mouth and is 
    made of glass. And in Britain, a flask is also a vacuum-sealed container that keeps drinks hot, usually called a 
    "Thermos" in the US. </p> 
    <br>
    <a href= "{}">Welcome</a>
</body>
</html>
""".format(name, age, image, url)
# anchor tag
# triple quotes
# mimetype = way of saying in HTML this is the type of document it is
if __name__ == "__main__":
    app.run(debug=True)
