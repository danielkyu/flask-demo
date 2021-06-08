from flask import Flask

import boto3
import os

app = Flask(__name__)

if os.environ.get('AWS_ENDPOINT_URL') is None:
  s3 = boto3.client('s3')
else:
  s3 = boto3.client('s3', endpoint_url = os.environ.get('AWS_ENDPOINT_URL'), use_ssl = False)

@app.route('/')
def index():
  print('ping!')
  return 'Web App with Python Flask!'

@app.route('/buckets')
def get_buckets():
  return ''.join(map(lambda bucket: bucket['Name'] + '\n', s3.list_buckets()['Buckets']))

app.run(host='0.0.0.0', port=os.environ.get('PORT'))

