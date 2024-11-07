import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()
category_tables = {
    "DS 4210": '''CREATE TABLE IF NOT EXISTS ds_4210_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "MKT 3400": '''CREATE TABLE IF NOT EXISTS ds_3400_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "DS 4220": '''CREATE TABLE IF NOT EXISTS ds_4220_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "DS 3850": '''CREATE TABLE IF NOT EXISTS ds_3850_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
    "DS 3860": '''CREATE TABLE IF NOT EXISTS ds_3860_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT
    )''',
}

# Create tables in the database
for table_creation_query in category_tables.values():
    cursor.execute(table_creation_query)
conn.commit()