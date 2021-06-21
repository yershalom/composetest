import requests
from flask import Flask

import logging
from sys import stdout

logger = logging.getLogger('app2')

logger.setLevel(logging.INFO)
logFormatter = logging.Formatter("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
consoleHandler = logging.StreamHandler(stdout)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

app = Flask(__name__)


def get_hit_count():
    resp = requests.get('http://app1.app1.svc.cluster.local:5000')
    logger.info('resp is: {}'.format(resp.text))
    return {'text': resp.text}


@app.route('/')
def hello():
    return get_hit_count()
