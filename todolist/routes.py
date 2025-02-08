from flask import Blueprint, render_template, request, redirect, url_for
from models import tasks 

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@routes.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)  
    return redirect(url_for("routes.index"))

@routes.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]  
    return redirect(url_for("routes.index"))
