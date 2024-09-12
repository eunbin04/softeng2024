from flask import Flask, request
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/hello/<name>')
def say_hello(name):
    return f"안녕하세요. {escape(name)}님."

@app.route('/dan/<dan>')
def gugudan_html(dan):
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan) * i}<br>"
    return html_str

@app.route('/gugudan/')
def gugudan_arg_html():
    dan = request.args.get("dan", "2")
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = <strong>{int(dan) * i}</strong><br>"
    return html_str


app.run(debug=True)