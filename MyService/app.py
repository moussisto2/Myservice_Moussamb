from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bonjour, je suis Moussamb!</h1><br><a href="https://www.example.com">Visitez mon site</a>'

if __name__ == '__main__':
    app.run(debug=True)
