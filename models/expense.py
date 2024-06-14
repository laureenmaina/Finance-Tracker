from models.__init__ import conn, cursor
from datetime import datetime

class Expense:

    def __init__(self, id, amount, date, user_id):
        self.id = id
        self.amount = amount
        self.date = date
        self.user_id = user_id


    @classmethod
    def create(cls, amount, user_id, date=None):
        
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        cursor.execute('SELECT SUM(amount) FROM incomes WHERE user_id = ?', (user_id,))

        total_income = cursor.fetchone()[0] or 0
        if amount > total_income:
            raise ValueError("Expense amount exceeds total income.")
        
        cursor.execute('INSERT INTO expenses (amount, date, user_id) VALUES (?, ?, ?)', (amount, date, user_id))
        conn.commit()
        return cursor.lastrowid
    

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM expenses')
        rows = cursor.fetchall()
        return [Expense(row[0], row[1], row[2], row[3]) for row in rows]
    

    @classmethod
    def find_by_id(cls, expense_id):
        cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
        row = cursor.fetchone()
        
        if row:
            return Expense(row[0], row[1], row[2], row[3])
        return None

    @classmethod
    def delete(cls, expense_id):
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
