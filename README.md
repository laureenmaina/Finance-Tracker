Finance Management System
Project Overview
The Finance Management System is a Python-based application that helps users manage their finances by tracking their incomes, expenses, and saving goals. The application uses SQLite as the database to store user information, income records, expense records, and saving goals. The database operations are performed using Python's sqlite3 module.

Features
User Management: Add and retrieve user information.
Income Management: Add and retrieve income records associated with users.
Expense Management: Add and retrieve expense records associated with users, ensuring expenses do not exceed total income.
Saving Goals: Add and retrieve saving goals associated with users, ensuring target dates are valid.

Project Structure
finance-management-system/
│
├── models/
│   ├── __init__.py
│   ├── setup.py
│   ├── user.py
│   ├── income.py
│   ├── expense.py
│   ├── saving_goal.py
│
├── main.py
├── README.md
└── requirements.txt

Models
User Model (models/user.py)

Attributes: id, username, email
Methods: create, get_all, find_by_id, delete
Income Model (models/income.py)

Attributes: id, amount, date, user_id
Methods: create, get_all, find_by_id, delete
Expense Model (models/expense.py)

Attributes: id, amount, date, user_id
Methods: create, get_all, find_by_id, delete
SavingGoal Model (models/saving_goal.py)

Attributes: id, amount, target_date, description, user_id
Methods: create, get_all, find_by_id, delete
Main Script (main.py)
This script initializes the database, collects user inputs, performs necessary validations, and interacts with the database using the defined models. It also prints out the stored records after performing the operations.

