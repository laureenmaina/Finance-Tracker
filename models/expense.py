from __init__ import conn,cursor,sqlite3
from datetime import datetime


class Expense:
    def __init__(self, id, amount, date, user_id):
        self.id = id
        self.amount = amount
        self.date = date
        self.user_id = user_id

    @staticmethod
    def create(amount, user_id, date=datetime.now().strftime('%Y-%m-%d')):
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT SUM(amount) FROM incomes WHERE user_id = ?', (user_id,))
        total_income = cursor.fetchone()[0] or 0

        if amount > total_income:
            raise ValueError("Expense amount exceeds total income.")
        
        cursor.execute('INSERT INTO expenses (amount, date, user_id) VALUES (?, ?, ?)', (amount, date, user_id))
        conn.commit()
        
        expense_id = cursor.lastrowid
        conn.close()
        return expense_id

    @staticmethod
    def get_all():
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()
        
        expenses = [Expense(row[0], row[1], row[2], row[3]) for row in rows]
        conn.close()
        return expenses