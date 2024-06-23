from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host= '0.0.0.0', port=8080, debug=True)