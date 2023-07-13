import wtforms
from wtforms.validators import Email, Length,EqualTo,InputRequired

from Utils.ResponseUtils import ResponseUtils
from exts import redis_client
from models import UserModel
from wtforms import validators


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[Length(4,4,message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(2,20,message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(2,20,message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[validators.EqualTo('password',message="两次密码不一致")])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="邮箱已被注册")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        stored_captcha = redis_client.get(email)

        if stored_captcha and stored_captcha.decode() == captcha:
            # Captcha is valid
            # Perform registration logic here
            redis_client.delete(email)  # Optional: Delete the captcha from Redis after successful verification
            # return ResponseUtils.success(message="captcha is valid")
            # raise wtforms.ValidationError(message="captcha is valid")
        # elif stored_captcha == -1:
        #     # Captcha expired
        #     # return ResponseUtils.error(message="captcha is expired")
        #     raise wtforms.ValidationError(message="captcha is expired or used")
        else:

            # Captcha is invalid or expired
            # return ResponseUtils.error(message="captcha is invalid")
            raise wtforms.ValidationError(message="captcha is expired or used")




class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[Length(2,20,message="密码错误")])

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(2,20,message="标题格式错误")])
    content = wtforms.StringField(validators=[Length(2,message="内容格式错误")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(2,message="内容格式错误")])

    question_id = wtforms.IntegerField(validators=[InputRequired(message="问题id不能为空")])