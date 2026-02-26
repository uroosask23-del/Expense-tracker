from expense_manager import *

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        add_expense(amount, category, date)
        print("Expense added ✔")

    elif choice == "2":
        expenses = view_expenses()
        for exp in expenses:
            print(exp)

    elif choice == "3":
        print("Total Expense:", total_expense())

    elif choice == "4":
        cat = input("Enter category: ")
        filtered = filter_by_category(cat)
        for exp in filtered:
            print(exp)

    elif choice == "5":
        break

    else:
        print("Invalid choice")