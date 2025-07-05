from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    if not task:
        return jsonify({"error": "Task field is required"}), 400
    tasks.append(task)
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    try:
        tasks.pop(index)
        return jsonify({"message": "Task deleted"}), 200
    except IndexError:
        return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
