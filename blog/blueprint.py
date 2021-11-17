from flask import Blueprint, render_template

from models import Post

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def posts():

    return render_template('blog/index.html', posts=Post.query.all())


@blog.route('/<slug>')
def post_detail(slug):

    post = Post.query.filter(Post.slug == slug).first()
    return render_template('blog/post_detail.html', post=post)
