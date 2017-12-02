from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create an app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

# Initialize bootstrap
bootstrap = Bootstrap(app)

# Class of the name form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')

# Home route
@app.route('/')
def index():
    return render_template("index.html")

# User route
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name = name)

# Form route
@app.route('/form', methods = ["GET", "POST"])
def nameform():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("nameform.html", name = name, form = form)

# Run the app
if __name__ == '__main__':
    app.run(debug = True)
