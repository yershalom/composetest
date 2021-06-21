import time

import redis
import requests
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    resp = requests.get('http://app1.app1.svc.cluster.local:5000')
    print('resp is: {}'.format(resp.text))
    return resp.text

@app.route('/')
def hello():
    return get_hit_count()
