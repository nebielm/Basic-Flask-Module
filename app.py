from flask import Flask
from flask import request, render_template, redirect, url_for
import json
import random

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.json", 'r') as dataobj:
        blog_posts = json.load(dataobj)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("author")
        with open("data.json", 'r') as dataobj:
            blog_posts = json.load(dataobj)
        id_is_unique = False
        while not id_is_unique:
            new_id = random.choice(range(len(blog_posts)+1, 100))
            if not any(blog['id'] == new_id for blog in blog_posts):
                id_is_unique = True
        new_blog = {"id": new_id, "author": author, "title": title, "content": content}
        blog_posts.append(new_blog)
        with open("data.json", 'w') as dataobj:
            json.dump(blog_posts, dataobj)
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
