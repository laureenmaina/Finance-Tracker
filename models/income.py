from models.__init__ import conn, cursor
from datetime import datetime

class Income:
    def __init__(self, id, amount, date, user_id):
        self.id = id
        self.amount = amount
        self.date = date
        self.user_id = user_id

    @classmethod
    def create(cls, amount, user_id, date=None):

        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        cursor.execute('INSERT INTO incomes (amount, date, user_id) VALUES (?, ?, ?)', (amount, date, user_id))
        conn.commit()
        return cursor.lastrowid

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM incomes')
        rows = cursor.fetchall()
        return [Income(row[0], row[1], row[2], row[3]) for row in rows]

    @classmethod
    def find_by_id(cls, income_id):
        cursor.execute('SELECT * FROM incomes WHERE id = ?', (income_id,))
        row = cursor.fetchone()
        
        if row:
            return Income(row[0], row[1], row[2], row[3])
        return None

    @classmethod
    def delete(cls, income_id):
        cursor.execute('DELETE FROM incomes WHERE id = ?', (income_id,))
        conn.commit()
