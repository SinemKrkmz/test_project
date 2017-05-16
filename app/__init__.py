from flask import Flask
from config import configuration


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(configuration.__dict__)
