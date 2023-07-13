from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

import redis

db = SQLAlchemy()
mail = Mail()




redis_client = redis.Redis(host='121.37.179.80', port=6379,password='zijian.redis')


