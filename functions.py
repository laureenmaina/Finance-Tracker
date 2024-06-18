from models.finance import session
from models.finance import User, Expense, Income, SavingGoal

# Create a new user
def create_user(username, email):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()

# Create a new expense
def create_expense(amount, description, user_id):
    new_expense = Expense(amount=amount, description=description, user_id=user_id)
    session.add(new_expense)
    session.commit()

# Create a new income
def create_income(amount, source, user_id):
    new_income = Income(amount=amount, source=source, user_id=user_id)
    session.add(new_income)
    session.commit()

# Create a new saving goal
def create_saving_goal(amount, goal_name, user_id):
    new_goal = SavingGoal(amount=amount, goal_name=goal_name, user_id=user_id)
    session.add(new_goal)
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