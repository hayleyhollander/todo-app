from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
next_id = 1 

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    data = request.get_json()
    task = {
        "id": next_id,
        "description": data["description"],
        "completed": False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            data = request.get_json()
            if "description" in data:
                task["description"] = data["description"]
            if "completed" in data:
                task["completed"] = data["completed"]
            return jsonify(task)
    return jsonify({"error": "Task not found"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"Task deleted"})
    return jsonify({"Task not found"})

if __name__ == "__main__":
    app.run(debug=True)
