from flask import Flask , request

app = Flask(__name__)


@app.route('/add')
def addition():
    return f"this is my test function"

@app.route('/shal')
def print_name():
    return f"Shalini"

@app.route('/username')
def print_username():
    data = request.args.get('name')
    return f"{data}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")

