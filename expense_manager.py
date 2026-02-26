import json
from datetime import datetime

FILE_NAME = "data.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount, category, date):
    expenses = load_expenses()

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)


def view_expenses():
    return load_expenses()


def total_expense():
    expenses = load_expenses()
    return sum(exp["amount"] for exp in expenses)


def filter_by_category(category):
    expenses = load_expenses()
    return [exp for exp in expenses if exp["category"] == category]
