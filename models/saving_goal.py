from __init__ import conn,cursor,sqlite3
from datetime import datetime



class SavingGoal:
    def __init__(self, id, amount, target_date, description, user_id):
        self.id = id
        self.amount = amount
        self.target_date = target_date
        self.description = description
        self.user_id = user_id

    @staticmethod
    def create(amount, user_id, target_date, description):
        if datetime.strptime(target_date, '%Y-%m-%d').date() < date.today():
            raise ValueError("Saving goal target date must be in the future.")

        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO saving_goals (amount, target_date, description, user_id) VALUES (?, ?, ?, ?)', 
                       (amount, target_date, description, user_id))
        conn.commit()
        
        saving_goal_id = cursor.lastrowid
        conn.close()
        return saving_goal_id

    @staticmethod
    def get_all():
        conn = sqlite3.connect('finance.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM saving_goals')
        rows = cursor.fetchall()
        
        saving_goals = [SavingGoal(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        conn.close()
        return saving_goals