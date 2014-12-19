from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/user/<string:name>')
def show_user(name):
    return 'The name is %s' % name

if __name__ == "__main__":
    app.run(debug = True)
