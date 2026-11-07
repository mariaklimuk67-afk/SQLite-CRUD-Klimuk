import sqlite3

def create_connection():
    return sqlite3.connect('data.db')

def create_db_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            genre TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_item(title, author, year, genre):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
                   (title, author, year, genre))
    conn.commit()
    conn.close()

def get_all_items():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    items = cursor.fetchall()
    conn.close()
    return items

def get_item_by_id(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item

def update_item(item_id, new_title, new_author, new_year, new_genre):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE id = ?",
                   (new_title, new_author, new_year, new_genre, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()