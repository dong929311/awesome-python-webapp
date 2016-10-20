import logging
from transwarp.web import get, view
from models import User, Blog, Comment


@view('test_user.html')
@get('/')
def test_users():
    users = User.findall()
    return dict(users=users)
