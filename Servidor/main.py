from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Kevin Márquez 8'

if __name__ == '__main__':
    app.run()