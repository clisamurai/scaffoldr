from flask import *
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)