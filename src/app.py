from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def index():
  print('XXXXXXXXXXXXX')
  return 'Web App with Python Flask!'

app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'))

