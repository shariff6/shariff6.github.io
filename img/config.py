from abc import abstractclassmethod
from flask import Flask
from instance.config import app_config
from twitter_ads.client import Client

app = Flask(__name__)
with app.app_context():
    app.config.from_object(app_config[app.config["ENV"]])
    CONSUMER_KEY = app.config["CONSUMER_KEY"]
    CONSUMER_SECRET = app.config["CONSUMER_SECRET"]
    ACCESS_TOKEN = app.config["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = app.config["ACCESS_TOKEN_SECRET"]
    ACCOUNT_ID = app.config["ACCOUNT_ID"]
    client = Client(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
