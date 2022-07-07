# Your First Website\

from exer50 import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "World"
    return 'Hello, {greeting}!'

if __name__ == "__main__":
    app.run()