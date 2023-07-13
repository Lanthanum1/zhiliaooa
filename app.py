
from flask import Flask, render_template,session,g
from flask_cors import CORS
from exts import db,mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate


import config



app = Flask(__name__)

CORS(app,origins='0.0.0.0')
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)


migrate = Migrate(app,db)
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# @app.route('/test')
# def test():
#     return 'test'

@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.filter_by(id=user_id).first()
        if user:
            g.user = user
    else:
        g.user = None

@app.context_processor
def context_processor():
    return {"user":g.user}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
