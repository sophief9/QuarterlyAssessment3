import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Define Question class
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

# Main application class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.selected_category = tk.StringVar()
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        # Load first window for category selection
        self.create_category_selection_window()

    def create_category_selection_window(self):
        tk.Label(self.root, text="Select a Category").pack(pady=10)

        # Get the available categories from the database
        categories = self.get_categories()

        # Ensure that categories are available
        if not categories:
            messagebox.showerror("No Categories", "No categories available in the database.")
            self.root.quit()
            return

        # Create dropdown menu with a limit of 5 categories
        category_menu = ttk.Combobox(self.root, textvariable=self.selected_category, values=categories)
        category_menu.pack(pady=5)
        tk.Button(self.root, text="Start Quiz Now", command=self.start_quiz).pack(pady=20)

    def get_categories(self):
        # Get the list of available categories by querying the table names
        try:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            # Extract categories, format them, and limit to the first 5
            categories = [
                table[0].replace('_questions', '').replace('_', '').upper() 
                for table in tables if table[0].endswith('_questions')
            ]
            return categories[:5]  # Limit to only 5 categories
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error fetching categories: {e}")
            return []

    def start_quiz(self):
        category = self.selected_category.get()
        if not category:
            messagebox.showwarning("Select Category", "Please select a category to start the quiz.")
            return

        # Fetch questions for the selected category
        self.fetch_questions(category)
        if not self.questions:
            messagebox.showerror("No Questions", "No questions available in this category.")
            return

        # Destroy category selection window and open quiz window
        for widget in self.root.winfo_children():
            widget.destroy()
        self.display_question()

    def fetch_questions(self, category):
        # Safely format the table name using double quotes for special characters or numbers
        table_name = f'"{category.lower()}_questions"'
        
        try:
            cursor.execute(f"SELECT question_text, option_a, option_b, option_c, option_d, correct_answer FROM {table_name}")
            questions_data = cursor.fetchall()
            self.questions = [
                Question(question_text=row[0], options=row[1:5], correct_answer=row[5]) for row in questions_data
            ]
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"Database error: {e}")
            print(f"Error executing query: {e}")
            return

    def display_question(self):
        if self.current_question_index >= len(self.questions):
            self.show_score()
            return

        question = self.questions[self.current_question_index]
        self.user_answer.set(None)

        # Display question and options
        tk.Label(self.root, text=question.question_text, font=("Arial", 14)).pack(pady=10)

        for i, option_text in enumerate(question.options):
            tk.Radiobutton(self.root, text=option_text, variable=self.user_answer, value=chr(65 + i)).pack(anchor='w')

        tk.Button(self.root, text="Submit Answer", command=self.submit_answer).pack(pady=20)

    def submit_answer(self):
        question = self.questions[self.current_question_index]
        user_answer = self.user_answer.get()

        if not user_answer:
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        # Check the answer
        if question.check_answer(user_answer):
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was: {question.correct_answer}")

        # Move to the next question
        self.current_question_index += 1

        # Clear window and show the next question
        for widget in self.root.winfo_children():
            widget.destroy()
        self.display_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score} out of {len(self.questions)}")
        self.root.quit()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()