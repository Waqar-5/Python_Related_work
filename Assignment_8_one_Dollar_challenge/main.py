
from flask import Flask, request, redirect, url_for, render_template_string, abort
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "habits.json"

class Habit:
    def __init__(self, name, history=None):
        self.name = name
        self.history = history or []

    def mark_done_today(self):
        today = datetime.today().strftime("%Y-%m-%d")
        if today not in self.history:
            self.history.append(today)

    def to_dict(self):
        return {"name": self.name, "history": self.history}

    @staticmethod
    def from_dict(data):
        return Habit(data["name"], data.get("history", []))

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        self.habits.append(Habit(name))

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def delete_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]

    def mark_done(self, name):
        habit = self.get_habit(name)
        if habit:
            habit.mark_done_today()

    def to_dict(self):
        return {"habits": [h.to_dict() for h in self.habits]}

    @staticmethod
    def from_dict(data):
        tracker = HabitTracker()
        for h_data in data.get("habits", []):
            tracker.habits.append(Habit.from_dict(h_data))
        return tracker

if os.path.exists(DATA_FILE):
    with open(DATA_FILE) as f:
        tracker = HabitTracker.from_dict(json.load(f))
else:
    tracker = HabitTracker()

@app.route("/")
def home():
    today = datetime.today().strftime("%Y-%m-%d")
    return render_template_string(HOME_TEMPLATE, habits=tracker.habits, today=today)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("habit")
    if name:
        tracker.add_habit(name)
        save_data()
    return redirect(url_for("home"))

@app.route("/done/<name>", methods=["POST"])
def mark_done(name):
    tracker.mark_done(name)
    save_data()
    return redirect(url_for("home"))

@app.route("/delete/<name>", methods=["POST"])
def delete(name):
    tracker.delete_habit(name)
    save_data()
    return redirect(url_for("home"))

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(tracker.to_dict(), f, indent=2)
    except Exception as e:
        print("Error saving:", e)

HOME_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Habit Tracker</title>
    <style>
        body { font-family: sans-serif; padding: 2rem; background: #f9f9f9; }
        h1 { color: #2c3e50; }
        form { margin-bottom: 1rem; }
        table { width: 100%%; border-collapse: collapse; background: #fff; }
        th, td { padding: 0.6rem; border: 1px solid #ccc; text-align: center; }
        button { padding: 0.4rem 0.8rem; margin: 0.2rem; }
        .done { background: #2ecc71; color: white; border: none; }
        .delete { background: #e74c3c; color: white; border: none; }
    </style>
</head>
<body>
    <h1>🧠 Daily Habit Tracker</h1>
    <form method="POST" action="/add">
        <input name="habit" placeholder="Enter a new habit" required>
        <button type="submit">Add Habit</button>
    </form>
    {% if habits %}
    <table>
        <tr>
            <th>Habit</th>
            <th>Days Done</th>
            <th>Done Today?</th>
            <th>Actions</th>
        </tr>
        {% for habit in habits %}
        <tr>
            <td>{{ habit.name }}</td>
            <td>{{ habit.history|length }}</td>
            <td>
                {% if today in habit.history %}
                    ✅
                {% else %}
                    <form method="POST" action="/done/{{ habit.name }}">
                        <button class="done">Mark Done</button>
                    </form>
                {% endif %}
            </td>
            <td>
                <form method="POST" action="/delete/{{ habit.name }}" onsubmit="return confirm('Delete this habit?');">
                    <button class="delete">Delete</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
        <p>No habits yet. Add one above! ✅</p>
    {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
