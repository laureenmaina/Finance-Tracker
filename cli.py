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
    print("1. Create User")
    print("2. Create Expense")
    print("3. Create Income")
    print("4. Create Saving Goal")
    print("5. View Users")
    print("6. View Expenses")
    print("7. View Incomes")
    print("8. View Saving Goals")
    print("9. Delete User")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            email = input("Enter email: ")
            create_user(username, email)
            print("User created!")

        elif choice == '2':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            user_id = int(input("Enter user ID: "))
            create_expense(amount, description, user_id)
            print("Expense created!")

        elif choice == '3':
            amount = float(input("Enter amount: "))
            source = input("Enter source: ")
            user_id = int(input("Enter user ID: "))
            create_income(amount, source, user_id)
            print("Income created!")

        elif choice == '4':
            amount = float(input("Enter amount: "))
            goal_name = input("Enter goal name: ")
            user_id = int(input("Enter user ID: "))
            create_saving_goal(amount, goal_name, user_id)
            print("Saving goal created!")

        elif choice == '5':
            users = get_all_users()
            print("\nUsers:")
            for user in users:
                print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

        elif choice == '6':
            expenses = get_all_expenses()
            print("\nExpenses:")
            for expense in expenses:
                print(f"ID: {expense.id}, Amount: {expense.amount}, Description: {expense.description}")

        elif choice == '7':
            incomes = get_all_incomes()
            print("\nIncomes:")
            for income in incomes:
                print(f"ID: {income.id}, Amount: {income.amount}, Source: {income.source}")

        elif choice == '8':
            saving_goals = get_all_saving_goals()
            print("\nSaving Goals:")
            for goal in saving_goals:
                print(f"ID: {goal.id}, Amount: {goal.amount}, Goal Name: {goal.goal_name}")

        elif choice == '9':
            user_id = int(input("Enter user ID: "))
            delete_user(user_id)
            print("User deleted!")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
