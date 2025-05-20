import json
import os
from flask import Flask, request, redirect, url_for, render_template_string, send_file, abort

app = Flask(__name__)

DATA_FILE = "budget_data.json"

# OOP Classes

class Transaction:
    _id_counter = 1

    def __init__(self, amount, category, description=""):
        self.id = Transaction._id_counter
        Transaction._id_counter += 1
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        t = Transaction(data["amount"], data["category"], data.get("description",""))
        t.id = data["id"]
        return t

class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t.id != transaction_id]

    def get_total(self):
        return sum(t.amount for t in self.transactions)

class BudgetTracker:
    def __init__(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)

    def add_transaction(self, category_name, amount, description=""):
        self.add_category(category_name)
        transaction = Transaction(amount, category_name, description)
        self.categories[category_name].add_transaction(transaction)
        return transaction.id

    def remove_transaction(self, transaction_id):
        for category in self.categories.values():
            before = len(category.transactions)
            category.remove_transaction(transaction_id)
            after = len(category.transactions)
            if before != after:
                # Remove empty category if no transactions left
                if len(category.transactions) == 0:
                    del self.categories[category.name]
                return True
        return False

    def get_summary(self):
        return {cat: category.get_total() for cat, category in self.categories.items()}

    def get_all_transactions(self):
        transactions = []
        for category in self.categories.values():
            transactions.extend(category.transactions)
        return transactions

    def to_dict(self):
        data = {}
        for cat_name, category in self.categories.items():
            data[cat_name] = [t.to_dict() for t in category.transactions]
        return data

    def from_dict(self, data):
        self.categories.clear()
        max_id = 0
        for cat_name, trans_list in data.items():
            cat = Category(cat_name)
            for tdata in trans_list:
                t = Transaction.from_dict(tdata)
                cat.add_transaction(t)
                if t.id > max_id:
                    max_id = t.id
            self.categories[cat_name] = cat
        Transaction._id_counter = max_id + 1

tracker = BudgetTracker()

# Load data from file if exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
            tracker.from_dict(data)
        except Exception as e:
            print("Failed to load data:", e)

# HTML Templates

summary_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Budget Tracker Summary</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background: #f0f2f5;}
        table {border-collapse: collapse; width: 50%;}
        th, td {border: 1px solid #ddd; padding: 8px; text-align:center;}
        th {background-color: #4CAF50; color: white;}
        a {text-decoration:none; color:#4CAF50; font-weight: bold;}
        a:hover {text-decoration:underline;}
        .container {max-width: 700px; margin:auto; background:white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #ccc;}
    </style>
</head>
<body>
<div class="container">
    <h1>Budget Summary</h1>
    {% if summary %}
    <table>
        <tr><th>Category</th><th>Total</th><th>Status</th></tr>
        {% for cat, total in summary.items() %}
        <tr>
            <td>{{ cat }}</td>
            <td>{{ "%.2f"|format(total) }}</td>
            <td>{{ 'Profit' if total >= 0 else 'Loss' }}</td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>No transactions yet. <a href="{{ url_for('add_transaction') }}">Add your first transaction</a>.</p>
    {% endif %}
    <p style="margin-top:20px;">
        <a href="{{ url_for('add_transaction') }}">Add Transaction</a> | 
        <a href="{{ url_for('transactions') }}">View All Transactions</a>
    </p>
</div>
</body>
</html>
"""

add_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Transaction</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background: #f0f2f5;}
        .container {max-width: 500px; margin:auto; background:white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #ccc;}
        label {display:block; margin-top: 15px;}
        input[type=text], input[type=number] {width: 100%; padding: 8px; margin-top: 5px; box-sizing: border-box; border-radius: 4px; border: 1px solid #ccc;}
        button {margin-top: 20px; padding: 10px 15px; background-color: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer;}
        button:hover {background-color: #45a049;}
        .error {color: red; margin-top: 10px;}
        a {text-decoration:none; color:#4CAF50; font-weight: bold;}
        a:hover {text-decoration:underline;}
    </style>
</head>
<body>
<div class="container">
    <h1>Add Transaction</h1>

    {% if error %}
    <p class="error">{{ error }}</p>
    {% endif %}

    <form method="POST">
        <label>Category:
            <input type="text" name="category" value="{{ category or '' }}" required>
        </label>
        <label>Amount (positive income, negative expense):
            <input type="text" name="amount" value="{{ amount or '' }}" required>
        </label>
        <label>Description:
            <input type="text" name="description" value="{{ description or '' }}">
        </label>
        <button type="submit">Add</button>
    </form>
    <p><a href="{{ url_for('home') }}">Back to Summary</a></p>
</div>
</body>
</html>
"""

transactions_html = """
<!DOCTYPE html>
<html>
<head>
    <title>All Transactions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background: #f0f2f5;}
        .container {max-width: 800px; margin:auto; background:white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px #ccc;}
        table {border-collapse: collapse; width: 100%;}
        th, td {border: 1px solid #ddd; padding: 8px; text-align:center;}
        th {background-color: #4CAF50; color: white;}
        form {display: inline;}
        button.delete-btn {
            background-color: #f44336; color: white; border: none; padding: 5px 10px; border-radius: 4px; cursor: pointer;
        }
        button.delete-btn:hover {background-color: #da190b;}
        a {text-decoration:none; color:#4CAF50; font-weight: bold;}
        a:hover {text-decoration:underline;}
    </style>
</head>
<body>
<div class="container">
    <h1>All Transactions</h1>
    {% if transactions %}
    <table>
        <tr><th>Category</th><th>Amount</th><th>Description</th><th>Type</th><th>Action</th></tr>
        {% for t in transactions %}
        <tr>
            <td>{{ t.category }}</td>
            <td>{{ "%.2f"|format(t.amount) }}</td>
            <td>{{ t.description }}</td>
            <td>{{ 'Income' if t.amount >= 0 else 'Expense' }}</td>
            <td>
                <form method="POST" action="{{ url_for('delete_transaction', transaction_id=t.id) }}" onsubmit="return confirm('Delete this transaction?');">
                    <button type="submit" class="delete-btn">Delete</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>No transactions recorded yet. <a href="{{ url_for('add_transaction') }}">Add a transaction</a>.</p>
    {% endif %}
    <p style="margin-top:20px;"><a href="{{ url_for('home') }}">Back to Summary</a></p>
</div>
</body>
</html>
"""

# Favicon: A simple 16x16 green circle encoded in base64 PNG
favicon_data = (
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAR0lEQVR4AWP4//8/AxTAwMDFV"
    "Y2DAyMDhT6MgpqAkBQRXBDKAki0ggK3CyRwGxWB0n8k0WMEuB0PES6ohSBBQNwDqB1RqoR4P"
    "ooODgaUDbIoP0HAZ8DShXIAAA4RgGwnhWnjwAAAABJRU5ErkJggg=="
)

@app.route('/favicon.ico')
def favicon():
    import base64
    from io import BytesIO
    from flask import send_file
    png = base64.b64decode(favicon_data)
    return send_file(BytesIO(png), mimetype='image/png')

# Routes

@app.route('/')
def home():
    summary = tracker.get_summary()
    return render_template_string(summary_html, summary=summary)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        category = request.form.get('category', '').strip()
        amount = request.form.get('amount', '').strip()
        description = request.form.get('description', '').strip()

        try:
            amount = float(amount)
            if category:
                tracker.add_transaction(category, amount, description)
                save_data()
                return redirect(url_for('home'))
            else:
                error = "Category cannot be empty."
        except ValueError:
            error = "Invalid amount. Please enter a number."
        
        return render_template_string(add_html, error=error, category=category, amount=amount, description=description)
    
    return render_template_string(add_html)

@app.route('/transactions')
def transactions():
    all_transactions = tracker.get_all_transactions()
    return render_template_string(transactions_html, transactions=all_transactions)

@app.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    success = tracker.remove_transaction(transaction_id)
    if success:
        save_data()
    else:
        abort(404)
    return redirect(url_for('transactions'))

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(tracker.to_dict(), f, indent=4)
    except Exception as e:
        print("Error saving data:", e)

if __name__ == '__main__':
    app.run(debug=True)
