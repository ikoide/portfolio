import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, Markup, send_from_directory
from flask_login import login_user, current_user, logout_user, login_required
from portfolio import app, db, bcrypt

@app.route("/")
def home():
    return render_template("index.html", title='Home')