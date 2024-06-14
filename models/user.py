from models.__init__ import conn, cursor

class User:

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @classmethod
    def create(cls, username, email):
        cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
        conn.commit()
        return cursor.lastrowid

    @classmethod
    def get_all(cls):
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        return [User(row[0], row[1], row[2]) for row in rows]

    @classmethod
    def find_by_id(cls, user_id):
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        
        if row:
            return User(row[0], row[1], row[2])
        return None

    @classmethod
    def delete(cls, user_id):
        
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
