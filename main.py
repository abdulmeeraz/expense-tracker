import json
import os
from datetime import datetime


def load_expenses(filename="expenses.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


def show_menu():
    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. View Expense by Category")
    print("5. Exit")


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, etc): ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for i, e in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{e['amount']} | {e['category']} | "
            f"{e['description']} | {e['date']}"
        )


def view_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"💰 Total Expense: ₹{total}")


def view_by_category(expenses):
    category = input("Enter category to filter: ").lower()
    filtered = [e for e in expenses if e["category"].lower() == category]

    if not filtered:
        print("No expenses found for this category.")
        return

    print(f"\n--- Expenses for {category.title()} ---")
    for e in filtered:
        print(f"₹{e['amount']} | {e['description']} | {e['date']}")


def expense_tracker_app():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            view_by_category(expenses)
        elif choice == "5":
            print("Goodbye! Expenses saved automatically 👍")
            break
        else:
            print("Invalid choice. Please try again.")


expense_tracker_app()
