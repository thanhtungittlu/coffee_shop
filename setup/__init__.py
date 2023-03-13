from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    def __init__(self):
        self.DATABASE = os.environ.get('DATABASE')
        self.USER_DATABASE = os.environ.get('USER_DATABASE')
        self.PASSWORD_DATABASE = os.environ.get('PASSWORD_DATABASE')
        self.SERVER_DATABASE = os.environ.get('SERVER_DATABASE')
        self.PORT_DATABASE = os.environ.get('PORT_DATABASE')


        self.SERVER_REDIS = os.environ.get('SERVER_REDIS')
        self.PORT_REDIS = os.environ.get('PORT_REDIS')

def load_config():
    try:
        config = Config()
        return config
    except Exception as e:
        print(e)
        return None
    
