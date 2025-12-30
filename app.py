from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Umer Farooq<br>i22-0518</h1>'

if __name__ == '__main__':
    app.run(debug=True)
