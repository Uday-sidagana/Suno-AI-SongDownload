from flask import Flask, Request, render_template, redirect, url_for



app = Flask(__name__, template_folder="Template")

@app.route('/')
def hello():
    return "Hello"


@app.route('/homepage')
def homepage():
    pass

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5020, debug=True)
