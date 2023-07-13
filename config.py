
SECRET_KEY = "123456"

# mysql database config
HOST = "121.37.179.80"
PORT = "3306"
USERNAME = "root"
PASSWORD = "68b4c97a78384721"
DATABASE = "zhiliaooa"
DB_URI= \
    "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# redis config
REDIS_HOST = "121.37.179.80"
REDIS_PORT = "6379"



# ogbhrwrgbzhaddda

# mail config
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "2834945633@qq.com"
MAIL_PASSWORD = "ogbhrwrgbzhaddda"
MAIL_DEFAULT_SENDER = "2834945633@qq.com"