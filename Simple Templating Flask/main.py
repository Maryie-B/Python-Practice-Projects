import os

from flask import Flask, render_template
from datetime import datetime
import requests
from dotenv import load_dotenv

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    return render_template('index.html', year=year)


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_response.json()
    age = age_data['age']
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_response.json()
    gender = gender_data['gender']
    year = datetime.now().year
    return render_template('guess.html', name=name, year=year, gender=gender, age=age)


@app.route('/blog')
def get_blog():
    load_dotenv()
    url = os.getenv("BLOG_URL")
    blog_response = requests.get(url)
    blog_data = blog_response.json()
    year = datetime.now().year
    return render_template('blog.html', year=year, blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)


