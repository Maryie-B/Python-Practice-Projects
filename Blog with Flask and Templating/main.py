import os

from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('URL')
posts = requests.get(url).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(f'{name}\n{email}\n{phone}\n{message}')
        return render_template("contact.html", post_request='Message sent successfully!')
    else:
        return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True, port=5001)
