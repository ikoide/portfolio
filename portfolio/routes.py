import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, Markup, send_from_directory
from flask_login import login_user, current_user, logout_user, login_required
from portfolio import app, db, bcrypt
from portfolio.forms import AdminForm, PostForm
from portfolio.models import Post

@app.route("/")
def home():
    return render_template("index.html", title='Home')

@app.route("/blog")
def blog():
    return render_template("blog.html", title='Blog')

@app.route("/blog/blog_page") # Change to actual blog with backend
def blog_page():
    return render_template("blog_page.html", title="Blog Page")

@app.route("/blog/posts/<int:post_id>")
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template("post.html", title=post.title, post=post, Markup=Markup)

@app.route("/blog/new_post", methods=['GET', 'POST'])
def new_post():
    postForm = PostForm()

    if postForm.validate_on_submit():
        post = Post(title=postForm.title.data, content=postForm.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))

    return render_template("admin/new_post.html", title="New Post", postForm=postForm, flash=flash)