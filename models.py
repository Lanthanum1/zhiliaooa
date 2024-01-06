from exts import db
from datetime import datetime

class UserModel(db.Model):
    # pass
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(2048),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    register_time = db.Column(db.DateTime,default=datetime.now,nullable=False)

class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('UserModel',backref=db.backref('questions'))
    # back_ref相当于在User模型中创建了一个questions属性，可以通过user id来获取他写过的所有questions

class AnswerModel(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now,nullable=False)

    question_id = db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    question = db.relationship('QuestionModel',backref=db.backref('answers',order_by=create_time.desc()))
    author = db.relationship('UserModel',backref=db.backref('answers'))