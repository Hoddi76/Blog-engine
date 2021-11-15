from flask import Blueprint, render_template

from models import Post


blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def post():
    posts = Post.query.all()
    return render_template('blog/index.html', posts=posts)
