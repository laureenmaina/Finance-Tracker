# Finance Management System

## Project Overview

The Finance Management System is a Python-based application designed to help users manage their finances by tracking incomes, expenses, and saving goals. The application utilizes SQLite as the backend database to store user information, income records, expense records, and saving goals. SQLAlchemy is used for ORM (Object-Relational Mapping) to interact with the SQLite database.

## Features

- **User Management**: Allows adding and retrieving user information.
- **Income Management**: Enables adding and retrieving income records associated with users.
- **Expense Management**: Facilitates adding and retrieving expense records associated with users, ensuring expenses do not exceed total income.
- **Saving Goals**: Supports adding and retrieving saving goals associated with users, ensuring target dates are valid.

## Project Structure

Certainly! Based on the updates made to your Finance Management System, let's revise the README.md file to reflect the changes:

markdown
Copy code
# Finance Management System

## Project Overview

The Finance Management System is a Python-based application designed to help users manage their finances by tracking incomes, expenses, and saving goals. The application utilizes SQLite as the backend database to store user information, income records, expense records, and saving goals. SQLAlchemy is used for ORM (Object-Relational Mapping) to interact with the SQLite database.

## Features

- **User Management**: Allows adding and retrieving user information.
- **Income Management**: Enables adding and retrieving income records associated with users.
- **Expense Management**: Facilitates adding and retrieving expense records associated with users, ensuring expenses do not exceed total income.
- **Saving Goals**: Supports adding and retrieving saving goals associated with users, ensuring target dates are valid.


│



## Models

### User Model

- **Attributes**: id, username, email
- **Methods**: create, get_all, find_by_id, delete

### Income Model

- **Attributes**: id, amount, date, user_id
- **Methods**: create, get_all, find_by_id, delete

### Expense Model 
- **Attributes**: id, amount, date, user_id
- **Methods**: create, get_all, find_by_id, delete

### SavingGoal Model 

- **Attributes**: id, amount, target_date, description, user_id
- **Methods**: create, get_all, find_by_id, delete

## Main Script (`cli.py`)

The main script initializes the database, collects user inputs, performs necessary validations, and interacts with the database using the defined models. It provides functionalities such as creating users, managing incomes, expenses, and saving goals, and displaying stored records after performing operations.


Data Persistence: Data entered through the application is stored persistently in the SQLite database (finance.db), ensuring data integrity and reliability