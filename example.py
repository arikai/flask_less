from flask import Flask, render_template
from flask_less import lessc
from atexit import register
from os import remove

app = Flask(__name__, template_folder='.')
lessc(app=app)

def cleanUp():
    try:
        remove('index.html')
    except Exception:
        pass

register(cleanUp)

@app.route('/')
def root():
    with open('index.html', 'w+') as file:
        file.write("<html><head>{{cssify('static/main.less')}}")
        file.write("</head><body><h1>Flask-Less Example !</body></html>")
    return render_template('index.html')


app.run(debug=True, port=4000)