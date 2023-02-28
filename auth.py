from flask import Blueprint

auth = Blueprint('auths', __name__)

@auth.route('/login')
def login():
    return "<p>Login<p>"


@auth.route('/logout')
def logout():
    return "<p>Logged Out </p>"


@auth.route('/signup')
def signup():
    return "<p>Sign up</p>"