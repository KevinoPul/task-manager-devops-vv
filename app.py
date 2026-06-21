from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

tasks = []
next_id = 1

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
</head>
<body>
    <h1>Task Manager - Gestión de Tareas</h1>

    <form method="POST" action="/add">
        <input type="text" name="title" placeholder="Nombre de la tarea">
        <select name="status">
            <option value="Pendiente">Pendiente</option>
            <option value="En progreso">En progreso</option>
            <option value="Completado">Completado</option>
        </select>
        <button type="submit">Crear tarea</button>
    </form>

    <hr>

    <h2>Lista de tareas</h2>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}

    <ul>
    {% for task in tasks %}
        <li>
            <form method="POST" action="/edit/{{ task.id }}" style="display:inline;">
                <input type="text" name="title" value="{{ task.title }}">
                <select name="status">
                    <option value="Pendiente" {% if task.status == "Pendiente" %}selected{% endif %}>Pendiente</option>
                    <option value="En progreso" {% if task.status == "En progreso" %}selected{% endif %}>En progreso</option>
                    <option value="Completado" {% if task.status == "Completado" %}selected{% endif %}>Completado</option>
                </select>
                <button type="submit">Editar</button>
            </form>

            <form method="POST" action="/delete/{{ task.id }}" style="display:inline;">
                <button type="submit">Eliminar</button>
            </form>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, tasks=tasks, error=None)

@app.route("/add", methods=["POST"])
def add_task():
    global next_id

    title = request.form.get("title", "").strip()
    status = request.form.get("status", "Pendiente")

    if title == "":
        return render_template_string(
            HTML,
            tasks=tasks,
            error="El nombre de la tarea no puede estar vacío."
        )

    task = {
        "id": next_id,
        "title": title,
        "status": status
    }

    tasks.append(task)
    next_id += 1

    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    title = request.form.get("title", "").strip()
    status = request.form.get("status", "Pendiente")

    if title == "":
        return render_template_string(
            HTML,
            tasks=tasks,
            error="No se puede editar una tarea con nombre vacío."
        )

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = title
            task["status"] = status
            break

    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)