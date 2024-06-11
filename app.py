from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open("data.json", 'r') as dataobj:
        blog_posts = json.load(dataobj)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run()
