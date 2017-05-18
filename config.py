import os


class DefaultConfig(object):
    def __init__(self):
        self.DEBUG = True
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))

        self.DATABASE_CONNECT_OPTIONS = {}
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.IS_PRODUCTION = False
        self.ACCESS_TOKEN_EXPIRE_TIME = 4  # hours
        self.WTF_CSRF_ENABLED = False

configuration = DefaultConfig()
