from flask import Flask

def create_app():
  app = Flask(__name__)
  app.secret_key = b'\xb1\x17\x1a>\xab!\xcb2\x04Go+\x10\xa9\xdd\xc5S\xae4\x1b\xf5#\xe4\xa1s\x1a\xf8l~\x1aF\xe1'
  return app
