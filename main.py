from flask import Flask

# Create an app
app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/<name>')
def user(name):
    return 'Hello %s!'%name

# Run the app
if __name__ == '__main__':
    app.run(debug = True)
