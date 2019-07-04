import os
class Config:
    """
    General configuration parent class
    """
    SECRET_KEY= os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://beryl:12345@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beryl:123@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://beryl:123@localhost/pitches'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

