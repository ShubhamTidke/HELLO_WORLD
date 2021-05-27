import re
from flask import Flask, request, render_template, redirect, url_for
from app import app, APP_ROOT


@app.route("/")
def index():
    return render_template("index.html")