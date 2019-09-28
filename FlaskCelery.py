# -*- coding: utf-8 -*-
from flask import Flask
from celery import Celery
import time
#
# from FlaskCelery import celery
from celery.result import AsyncResult

app = Flask(__name__)

app.config["CELERY_BROKER_URL"] = "redis://:redis@127.0.0.1:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://:redis@127.0.0.1:6379/1"

# app.config_from_object('celeryconfig')

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)


@app.route("/")
def index():
    return "index"


@app.route("/sum/<a>/<b>")
def sum_(a, b):
    result = back_group_task.delay(int(a), int(b))
    # 返回任务id
    return result.id


@app.route("/get_result/<result_id>")
def get_result(result_id):
    result = AsyncResult(id=result_id)
    return str(result.get())


@celery.task
def back_group_task(a, b):
    time.sleep(5)
    return a + b


if __name__ == '__main__':
    print app.url_map
    app.run(host="0.0.0.0", port=7878)
