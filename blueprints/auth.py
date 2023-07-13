from flask import Blueprint, render_template,request,redirect,url_for,session
from exts import mail, redis_client, db
from flask_mail import Message
from Utils.ResponseUtils import ResponseUtils
from models import UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random
bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register',methods=['GET','POST'])
def register():
    # pass
    if request.method == 'GET':
        return render_template('register.html')
    # return 'register'
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))

            # return ResponseUtils.success(message="register success")
        else:
            print(form.errors)
            return ResponseUtils.error(message=f"register failed,{form.errors}")
            # return redirect(url_for("auth.register"))
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password,password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                return ResponseUtils.error(message=f"login failed,{form.errors}")
    # return render_template('login.html')
    # pass

@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@bp.route('/captcha/email',methods=['POST'])
def mail_captcha():
    email = request.args.get('email')
    captcha_len = 4
    source = string.ascii_letters + string.digits
    captcha = ''.join(random.sample(source, captcha_len))
    message = Message('captcha test', recipients=[email],
                      body=f'Your captcha is: {captcha}')
    mail.send(message)
    redis_client.set(email, captcha,ex=3000)
    # print(captcha)
    # return captcha
    return ResponseUtils.success(data=captcha,message="send captcha success")
@bp.route('/verify')
def verify_captcha():
    email = request.args.get('email')
    user_captcha = request.args.get('captcha')
    stored_captcha = redis_client.get(email)

    if stored_captcha and stored_captcha.decode() == user_captcha:
        # Captcha is valid
        # Perform registration logic here
        redis_client.delete(email)  # Optional: Delete the captcha from Redis after successful verification
        return ResponseUtils.success(message="captcha is valid")
    else:
        # Captcha is invalid or expired
        return ResponseUtils.error(message="captcha is invalid")


@bp.route('mail/test')
def mail_test():
    # return 'test'
    # pass
    message = Message('mail test', recipients=['1707971622@qq.com'],
                      body='The function of this message is to test the mail')
    mail.send(message)
    return "send success"