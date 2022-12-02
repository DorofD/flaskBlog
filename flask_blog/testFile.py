import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn



conn = get_db_connection()
posts = conn.execute('SELECT * FROM posts').fetchall()
print(f'{posts[0][0]} {posts[0][1]} {posts[0][2]}')
print(f'{posts[1][0]} {posts[1][1]} {posts[1][2]}')
conn.close()
