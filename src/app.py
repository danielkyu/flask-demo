from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def index():
  print('ping!')
  return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=os.environ.get('PORT'))

