from flask import Flask
from flask import render_template
import os

schedule_api_consumer_key = 'BvOZK5KG6QyMfnHY5_jTaodOC0Qa'
schedule_api_secret_key   = 'fN2e8ZwtzUBebTmvYTfrh7N3irga'
app = Flask(__name__)

app.secret_key = os.urandom(24)