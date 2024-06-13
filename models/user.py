from models.__init__ import conn,cursor,sqlite3


class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
        

    @staticmethod
    def create(username, email):
        from models.__init__ import cursor,conn
        
        cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
        conn.commit()
        
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    @staticmethod
    def get_all():
        from models.__init__ import cursor,conn
        
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        
        users = [User(row[0], row[1], row[2]) for row in rows]
        conn.close()
        return users