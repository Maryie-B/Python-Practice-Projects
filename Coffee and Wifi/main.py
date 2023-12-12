import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, URL
import csv
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('KEY')
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    location = StringField('location', validators=[DataRequired(), URL()])
    open_time = StringField('open', validators=[DataRequired()])
    close_time = StringField('close',  validators=[DataRequired()])
    coffe_rating = SelectMultipleField('coffee', choices=[('1', '☕️'), ('2', '☕️ ☕️'), ( '3', '☕️ ☕️ ☕️'),
                                                          ('4', '☕️ ☕️ ☕️ ☕️'), ('5', '☕️ ☕️ ☕️ ☕️ ☕️')],
                                                            validators=[DataRequired()])
    wifi_rating = SelectMultipleField('wifi', choices=[('1', '💪'), ('2', '💪 💪'), ( '3', '💪 💪 💪'),
                                                          ('4', '💪 💪 💪 💪'), ('5', '💪 💪 💪 💪 💪')],
                                                            validators=[DataRequired()])


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
