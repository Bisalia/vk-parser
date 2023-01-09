from flask import Flask
import redis 
from rq import Queue

app_1=Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)



from app_1 import views

from app_1 import tasks
