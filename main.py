from models.user import User
from models.income import Income
from models.expense import Expense
from models.saving_goal import SavingGoal
from datetime import datetime
from models.setup import create_tables

def main():
  
    create_tables()

    # Collect user input
    username = str(input("Enter User's name: "))
    email = str(input("Enter User's email: "))
    income_amount = float(input("Enter your income: "))
    expense_amount = float(input("Enter your expense: "))
    saving_goal_amount = float(input("Enter your saving goal: "))
    saving_goal_target_date = input("Enter saving goal target date (YYYY-MM-DD): ")
    saving_goal_description = str(input("Enter saving goal description: "))

    if not username.strip():  # Check if username is empty 
        raise ValueError("Username cannot be empty")
    
    if not isinstance(username, str):
        raise ValueError("Username must be a string")

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
    except ValueError as error:
        print(f"Error: {error}")
        return

    # Create and add saving goal
    try:
        SavingGoal.create(amount=saving_goal_amount, user_id=user_id, target_date=saving_goal_target_date, description=saving_goal_description)
        
    except ValueError as error:
        print(f"Error: {error}")
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
