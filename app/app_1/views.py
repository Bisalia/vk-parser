from app_1 import app_1
from app_1.tasks import count_words
from app_1 import r 
from app_1 import q


from flask import  render_template,  request

from time import strftime



@app_1.route("/")

def index():
    return "Hello World"

@app_1.route("/add-task", methods=["GET", "POST"])

def add_task():

    
    jobs = q.jobs
    message=None

    if request.args:
        url =request.args.get("url")
        task = q.enqueue(count_words, url)

        jobs = q.jobs

        q_len = len(q)
        message = f"Task enqueued at {task.enqueued_at.strftime('%a %d %b %Y %H:%M:%S')}, {q_len} jobs queued"
    

    return render_template("add_task.html", message=message, jobs=jobs)


