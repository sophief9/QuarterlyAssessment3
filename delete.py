import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Function to delete a question by its ID or question text
def delete_question_from_table(subject_table, question_id_or_text):
    try:
        # Check if the input is a number (i.e., question ID)
        if question_id_or_text.isdigit():
            cursor.execute(f'SELECT * FROM {subject_table} WHERE id = ?', (question_id_or_text,))
        else:
            cursor.execute(f'SELECT * FROM {subject_table} WHERE question = ?', (question_id_or_text,))

        question = cursor.fetchone()

        if not question:
            print(f"No question found with that ID or text in {subject_table}.")
            return
        
        # Ask for confirmation
        confirm = input(f"Are you sure you want to delete the question: '{question[1]}'? (y/n): ")
        if confirm.lower() == 'y':
            if question_id_or_text.isdigit():
                cursor.execute(f'DELETE FROM {subject_table} WHERE id = ?', (question_id_or_text,))
            else:
                cursor.execute(f'DELETE FROM {subject_table} WHERE question = ?', (question_id_or_text,))
            conn.commit()
            print(f"Question '{question[1]}' has been deleted from {subject_table}.")
        else:
            print("Deletion canceled.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # List of subjects and their corresponding tables
    subjects = [
        ('DS4210', 'Business Intelligence'),
        ('MKT3400', 'Principles of Marketing'),
        ('DS4220', 'Advanced Analytics'),
        ('DS3850', 'Business Applications Develop'),
        ('DS3860', 'Business Database Management')
    ]
    
    # Ask the user to choose a subject
    print("Select a subject to delete a question from:")
    for i, (table, name) in enumerate(subjects, 1):
        print(f"{i}. {name}")
    
    try:
        subject_choice = int(input("Enter the number corresponding to the subject: "))
        if subject_choice < 1 or subject_choice > len(subjects):
            print("Invalid selection.")
            return
        
        # Get the selected subject's table name
        selected_subject = subjects[subject_choice - 1][0]

        # Display all questions in the selected table
        cursor.execute(f"SELECT * FROM {selected_subject}")
        questions = cursor.fetchall()

        if questions:
            print(f"\nQuestions in {selected_subject}:")
            for q in questions:
                print(f"ID: {q[0]}, Question: {q[1]}")
        else:
            print(f"No questions found in {selected_subject}.")
            return

        # Get the question ID or text to delete
        question_id_or_text = input(f"\nEnter the question ID or the full question text to delete from {selected_subject}: ")

        # Call the delete function for the selected subject table
        delete_question_from_table(selected_subject, question_id_or_text)

    except ValueError:
        print("Please enter a valid number.")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()
