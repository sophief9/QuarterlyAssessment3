import sqlite3

def get_table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

def display_questions(cursor, table_name):
    cursor.execute(f"SELECT rowid, * FROM {table_name}")
    questions = cursor.fetchall()
    
    if questions:
        print(f"\nQuestions in {table_name}:")
        for q in questions:
            print(f"ID: {q[0]}, Question: {q[1]}")
        return True
    else:
        print(f"No questions found in {table_name}.")
        return False

def delete_question(cursor, conn, table_name, question_id):
    cursor.execute(f"SELECT question_text FROM {table_name} WHERE rowid = ?", (question_id,))
    question = cursor.fetchone()

    if question:
        confirm = input(f"Are you sure you want to delete the question: '{question[0]}'? (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ?", (question_id,))
            conn.commit()
            print("Question has been deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("No question found with that ID.")

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    
    try:
        # Get and display all table names
        tables = get_table_names(cursor)
        print("Available tables:")
        for i, table in enumerate(tables, 1):
            print(f"{i}. {table}")
        
        # Select a table
        table_choice = int(input("\nEnter the number corresponding to the table you want to delete a question from: ")) - 1
        if table_choice < 0 or table_choice >= len(tables):
            print("Invalid selection.")
            return

        selected_table = tables[table_choice]

        # Display all questions in the selected table
        if display_questions(cursor, selected_table):
            # Select a question ID to delete
            question_id = input("\nEnter the ID of the question you want to delete: ")
            if question_id.isdigit():
                delete_question(cursor, conn, selected_table, int(question_id))
            else:
                print("Invalid ID entered.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
