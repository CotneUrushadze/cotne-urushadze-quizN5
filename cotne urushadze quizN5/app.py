from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    tasks = ["gaigvidze", "wame", "wadi mziurshi", "qvizi were"]

    return render_template("index.html", my_tasks=tasks)


@app.route('/add_task')
def add_task():
    return render_template("add_task.html")



if __name__ == '__main__':
    app.run(debug=True)

