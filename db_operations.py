# db_operations.py
import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def get_all_books(self):
        query = "SELECT * FROM books"
        self.cur.execute(query)
        return self.cur.fetchall()

    def create_book(self, data):
        query = "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)"
        self.cur.execute(query, data)
        self.conn.commit()

    def update_book(self, data):
        query = "UPDATE books SET title = %s, author = %s, published_year = %s WHERE id = %s"
        self.cur.execute(query, data)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
