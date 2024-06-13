from models.__init__ import conn,cursor,sqlite3
from datetime import datetime


class Income:
    def __init__(self, id, amount, date, user_id):
        self.id = id
        self.amount = amount
        self.date = date
        self.user_id = user_id

    @staticmethod
    def create(amount, user_id, date=datetime.now().strftime('%Y-%m-%d')):
        from models.__init__ import cursor,conn
        
        cursor.execute('INSERT INTO incomes (amount, date, user_id) VALUES (?, ?, ?)', (amount, date, user_id))
        conn.commit()
        
        income_id = cursor.lastrowid
        conn.close()
        return income_id

    @staticmethod
    def get_all():
        from models.__init__ import cursor,conn
        
        cursor.execute('SELECT * FROM incomes')
        rows = cursor.fetchall()
        
        incomes = [Income(row[0], row[1], row[2], row[3]) for row in rows]
        conn.close()
        return incomes