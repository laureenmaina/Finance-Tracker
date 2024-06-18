from datetime import datetime
from functions import (
    create_user,
    create_expense,
    create_income,
    create_saving_goal,
    get_all_users,
    get_all_expenses,
    get_all_incomes,
    get_all_saving_goals,
    delete_user
)

def menu():
    print("\nFinance Management System")
    print("1. Add User")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. Add Saving Goal")
    print("5. View Users")
    print("6. View Expenses")
    print("7. View Incomes")
    print("8. View Saving Goals")
    print("9. Delete User and Their Records")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")

            try:
                create_user(username, email)
                print("User added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == '2':
            amount = float(input("Enter income amount: "))
            date = datetime.strptime(input("Enter income date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            user_id = int(input("Enter user ID: "))

            try:
                create_income(amount, date, user_id)
                print("Income added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == '3':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            user_id = int(input("Enter user ID: "))

            try:
                create_expense(amount, user_id, description)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == '4':
            amount = float(input("Enter saving goal amount: "))
            target_date = datetime.strptime(input("Enter target date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            description = input("Enter saving goal description: ")
            user_id = int(input("Enter user ID: "))

            try:
                create_saving_goal(amount, target_date, description, user_id)
                print("Saving goal added successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == '5':
            users = get_all_users()
            print("\nUsers:")
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

        elif choice == '6':
            expenses = get_all_expenses()
            print("\nExpenses:")
            for expense in expenses:
                print(f"ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, User ID: {expense.user_id}")

        elif choice == '7':
            incomes = get_all_incomes()
            print("\nIncomes:")
            for income in incomes:
                print(f"ID: {income.id}, Amount: {income.amount}, Date: {income.date}, User ID: {income.user_id}")

        elif choice == '8':
            saving_goals = get_all_saving_goals()
            print("\nSaving Goals:")
            for goal in saving_goals:
                print(f"ID: {goal.id}, Amount: {goal.amount}, Target Date: {goal.target_date}, Description: {goal.description}, User ID: {goal.user_id}")

        elif choice == '9':
            user_id = int(input("Enter user ID to delete: "))
            try:
                delete_user(user_id)
                print("User and associated records deleted successfully!")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
