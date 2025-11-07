#!/usr/bin/env python
# coding: utf-8

# ---
# ### Import Libraries
# ---

# In[3]:


from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Task


# ---
# ### routes
# ---

# In[4]:


# Blueprint registration
tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

# Allowed enum values
VALID_STATUSES = ["todo", "in_progress", "done"]
VALID_PRIORITIES = ["low", "medium", "high"]

# ------------------------------------------------------------
# GET /tasks
# ------------------------------------------------------------
@tasks_bp.route("/", methods=["GET"])
def get_tasks():
    status = request.args.get("status")
    priority = request.args.get("priority")
    sort_by = request.args.get("sort_by", "created_at")
    order = request.args.get("order", "asc")

    query = Task.query

    # Filtering
    if status:
        if status not in VALID_STATUSES:
            return jsonify({"error": f"Invalid status. Must be one of {VALID_STATUSES}"}), 400
        query = query.filter_by(status=status)

    if priority:
        if priority not in VALID_PRIORITIES:
            return jsonify({"error": f"Invalid priority. Must be one of {VALID_PRIORITIES}"}), 400
        query = query.filter_by(priority=priority)

    # Sorting
    if hasattr(Task, sort_by):
        if order == "desc":
            query = query.order_by(db.desc(getattr(Task, sort_by)))
        else:
            query = query.order_by(db.asc(getattr(Task, sort_by)))
    else:
        return jsonify({"error": f"Invalid sort field: {sort_by}"}), 400

    tasks = query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


# ------------------------------------------------------------
# GET /tasks/<id>
# ------------------------------------------------------------
@tasks_bp.route("/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200


# ------------------------------------------------------------
# POST /tasks
# ------------------------------------------------------------
@tasks_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()

    # Validation
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    title = data["title"]
    description = data.get("description", "")
    status = data.get("status", "todo").strip().lower()
    priority = data.get("priority", "medium").strip().lower()

    if len(title) > 200:
        return jsonify({"error": "Title max length is 200"}), 400

    if status not in VALID_STATUSES:
        return jsonify({"error": f"Invalid status. Must be one of {VALID_STATUSES}"}), 400

    if priority not in VALID_PRIORITIES:
        return jsonify({"error": f"Invalid priority. Must be one of {VALID_PRIORITIES}"}), 400

    # Create and save task
    new_task = Task(
        title=title,
        description=description,
        status=status,
        priority=priority,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201


# ------------------------------------------------------------
# PUT /tasks/<id>
# ------------------------------------------------------------
@tasks_bp.route("/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "title" in data:
        if len(data["title"]) > 200:
            return jsonify({"error": "Title max length is 200"}), 400
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({"error": f"Invalid status. Must be one of {VALID_STATUSES}"}), 400
        task.status = data["status"]

    if "priority" in data:
        if data["priority"] not in VALID_PRIORITIES:
            return jsonify({"error": f"Invalid priority. Must be one of {VALID_PRIORITIES}"}), 400
        task.priority = data["priority"]

    task.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify(task.to_dict()), 200


# ------------------------------------------------------------
# DELETE /tasks/<id>
# ------------------------------------------------------------
@tasks_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200


# In[ ]:




