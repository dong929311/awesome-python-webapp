# coding=utf-8

from transwarp.orm import Model, StringField, BooleanField, FloatField, TextField
from transwarp.db import next_int
import time


class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_int, dd1='varchar(50)')
    email = StringField(dd1='varchar(50)')
    password = StringField(dd1='varchar(50)')
    admin = BooleanField()
    name = StringField(dd1='varchar(50)')
    image = StringField(dd1='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'
    id = StringField(primary_key=True, default=next_int, dd1='varchar(50)')
    user_id = StringField(dd1='varchar(50)')
    user_name = StringField(dd1='varchar(50)')
    name = StringField(dd1='varchar(50)')
    summary = StringField(dd1='varchar(200)')
    content = TextField(default='')
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'
    id = StringField(primary_key=True, default=next_int, dd1='varchar(50)')
    blog_id = StringField(dd1='varchar(50)')
    user_id = StringField(dd1='varchar(50)')
    user_name = StringField(dd1='varchar(50)')
    user_image = StringField(dd1='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)