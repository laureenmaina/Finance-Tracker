from models.finance import session
from models.finance import User, Expense, Income, SavingGoal
from datetime import datetime

# Create a new user
def create_user(username, email):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()

# Create a new expense
def create_expense(amount,user_id, description):
    user = session.query(User).get(user_id)
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")


    # Get total income (salary) for the user
    total_income = sum(income.amount for income in user.incomes)

    # Check if expense amount exceeds income
    if amount > total_income:
        raise ValueError("Expense amount cannot exceed total income")

    new_expense = Expense(amount=amount, user_id=user_id, description=description)
    session.add(new_expense)
    session.commit()

# Create a new income
def create_income(amount, source, user_id):
    new_income = Income(amount=amount, source=source, user_id=user_id)
    session.add(new_income)
    session.commit()

# Create a new saving goal
def create_saving_goal(amount, target_date, description, user_id):
    user = session.query(User).get(user_id)
    if not user:
        raise ValueError(f"User with ID {user_id} does not exist.")
    
    new_saving_goal = SavingGoal(amount=amount, target_date=target_date, description=description, user_id=user_id)
    session.add(new_saving_goal)
    session.commit()

    # Ensure target date is not in the past
    if target_date < datetime.now().date():
        raise ValueError("Target date cannot be in the past")

    new_saving_goal = SavingGoal(amount=amount, target_date=target_date, description=description, user_id=user_id)
    session.add(new_saving_goal)
    session.commit()

# Retrieve all users
def get_all_users():
    return session.query(User).all()

# Retrieve all expenses
def get_all_expenses():
    return session.query(Expense).all()

# Retrieve all incomes
def get_all_incomes():
    return session.query(Income).all()

# Retrieve all saving goals
def get_all_saving_goals():
    return session.query(SavingGoal).all()

# Delete a user and cascade delete their related records (expenses, incomes, saving goals)
def delete_user(user_id):
    user = session.query(User).get(user_id)
    session.delete(user)
    session.commit()