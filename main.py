from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap


# Create an app
app = Flask(__name__)

# Initialize bootstrap
bootstrap = Bootstrap(app)

# Home route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>')
def user(name):
    return render_template("user.html", name = name)

# Run the app
if __name__ == '__main__':
    app.run(debug = True)
