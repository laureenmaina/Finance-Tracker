from models import create_tables, User, Income, Expense, SavingGoal
from datetime import datetime,date

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    username = input("Enter User's name: ")
    email = input("Enter User's email: ")
    income_amount = float(input("Enter your income: "))
    expense_amount = float(input("Enter your expense: "))
    saving_goal_amount = float(input("Enter your saving goal: "))
    saving_goal_target_date = input("Enter saving goal target date (YYYY-MM-DD): ")
    saving_goal_description = input("Enter saving goal description: ")

    # Validate the target date
    try:
        datetime.strptime(saving_goal_target_date, '%Y-%m-%d')
    except ValueError:
        print("Error: Invalid date format.")
        return

    # Create and add user
    user_id = User.create(username=username, email=email)

    # Create and add income
    Income.create(amount=income_amount, user_id=user_id)

    # Validate and create expense
    try:
        Expense.create(amount=expense_amount, user_id=user_id)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create and add saving goal
    try:
        SavingGoal.create(amount=saving_goal_amount, user_id=user_id, target_date=saving_goal_target_date, description=saving_goal_description)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Query the database for inserted records
    users = User.get_all()
    incomes = Income.get_all()
    expenses = Expense.get_all()
    saving_goals = SavingGoal.get_all()

    # Display results
    print("\nUsers:")
    for user in users:
        print(user.__dict__)

    print("\nIncomes:")
    for income in incomes:
        print(income.__dict__)

    print("\nExpenses:")
    for expense in expenses:
        print(expense.__dict__)

    print("\nSaving Goals:")
    for saving_goal in saving_goals:
        print(saving_goal.__dict__)

if __name__ == "__main__":
    main()
