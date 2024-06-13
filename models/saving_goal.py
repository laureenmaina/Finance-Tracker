from models.__init__ import conn, cursor
from datetime import datetime, date

class SavingGoal:
    def __init__(self, id, amount, target_date, description, user_id):
        self.id = id
        self.amount = amount
        self.target_date = target_date
        self.description = description
        self.user_id = user_id

    @classmethod
    def create(cls, amount, user_id, target_date, description):
        if datetime.strptime(target_date, '%Y-%m-%d').date() < date.today():
            raise ValueError("Saving goal target date must be in the future.")
        cursor.execute('INSERT INTO saving_goals (amount, target_date, description, user_id) VALUES (?, ?, ?, ?)', 
                       (amount, target_date, description, user_id))
        conn.commit()
        return cursor.lastrowid

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM saving_goals')
        rows = cursor.fetchall()
        return [SavingGoal(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    @classmethod
    def find_by_id(cls, saving_goal_id):
        cursor.execute('SELECT * FROM saving_goals WHERE id = ?', (saving_goal_id,))
        row = cursor.fetchone()
        if row:
            return SavingGoal(row[0], row[1], row[2], row[3], row[4])
        return None

    @classmethod
    def delete(cls, saving_goal_id):
        cursor.execute('DELETE FROM saving_goals WHERE id = ?', (saving_goal_id,))
        conn.commit()
