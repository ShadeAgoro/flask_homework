from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def say_hello_page(name):
    return """
<html>
<head>
    <title>Sample - Flask routes/title>
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
</body>
</html>
""".format(name)
# triple quote marks displays data over multiple lines



if __name__ == "__main__":
    app.run(debug=True)
