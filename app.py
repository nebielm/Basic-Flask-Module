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


@app.route('/delete/<int:post_id>', methods=["POST"])
def delete(post_id):
    with open("data.json", "r") as dataobj:
        blog_posts = json.load(dataobj)
    for post in blog_posts:
        if post["id"] == post_id:
            blog_posts.remove(post)
            break
    with open("data.json", "w") as dataobj:
        json.dump(blog_posts, dataobj)
    return render_template("index.html", posts=blog_posts)


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
    # Update the post in the JSON file
    # Redirect back to index

    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run()
