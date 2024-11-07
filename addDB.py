#this creates new tables and adds the questions to the tables.

#if want a new table, use the code below to format and add questions

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Sample data (added new categories DS 4220, DS 3850, DS 3860)
sample_data = {
    "DS4210": [
        ("What does BI stand for?", "Business Information", "Business Intelligence", "Basica Information", "Business Integration", "B"),
        ("Which tool is commonly used for data visualization?", "SQL", "Power BI", "Java", "Python", "B"),
        ("What is a data warehouse?", "A place for storing web pages", "A large repository of historical data for analysis", "A type of database for managing transactions", "A tool for programming", "B"),
        ("What does OLAP stand for?", "Online Analytical Processing", "Online Application Processing", "Online Access Processing", "Online Analytical Processing", "A"),
        ("Which is the primary goal of ETL?", "Analyze data", "Visualize data", "Query data", "Extract, Transform, Load", "D"),
        ("Which of these is a typical BI data source?", "Transactional databases", "Text files", "Web scraping tools", "All of the above", "D"),
        ("What does data mining involve?", "Cleaning data", "Storing data", "Discovering patterns in data", "Backing up data", "C"),
        ("Which BI tool is used for reporting?", "Excel", "R", "Tableau", "All of the above", "D"),
        ("What is a KPI?", "Key Personal Indicator", "Key Performance Indicator", "Known Process Indicator", "Known Performance Indicator", "B"),
        ("What is the main purpose of a dashboard in BI?", "To store data", "To visualize data", "To clean data", "To query data", "B"),
    ],
    "MKT3400": [
        ("What is marketing?", "Selling products", "Understanding customer needs", "Creating ads", "Designing logos", "B"),
        ("What is an example of direct marketing?", "TV Commericals", "Social Media ads", "Billboards", "Email campaigns", "D"),
        ("What are the 4 Ps of marketing?", "Product, Price, Promotion, Place", "People, Product, Price, Promotion", "Product, Price, Publicity, Place", "Price, Product, People, Promotion", "A"),
        ("What is market segmentation?", "Dividing the market into groups", "Targeting the whole market", "Advertising to everyone", "Selling at a higher price", "A"),
        ("What does branding refer to?", "A product's price", "A store's logo", "A product's identity", "The promotion method used", "C"),
        ("What is a target market?", "A group of similar customers", "All people in the world", "Only high-income individuals", "A competitor's customers", "A"),
        ("What is a marketing strategy?", "A sales pitch", "A plan to reach target customers", "A type of advertisement", "A product's feature", "B"),
        ("What is the role of advertising in marketing?", "To reduce costs", "To persuade customers to buy", "To create competition", "To manage inventory", "B"),
        ("What is digital marketing?", "Television ads", "Social media marketing", "Billboards", "Word-of-mouth marketing", "B"),
        ("What is a product?", "Something that is sold", "A type of ad", "A competitor's brand", "A market segment", "A"),
    ],
    "DS4220": [
        ("What is the function to create a vector in R?", "vector()", "c()", "list()", "array()", "B"),
        ("Which function is used to calculate the mean in R?", "average()", "mean()", "sum()", "median()", "B"),
        ("How do you install a package in R?", "install.packages()", "library()", "require()", "usePackage()", "A"),
        ("Which function is used to read a CSV file in R?", "read.table()", "read.csv()", "read()","csv.read()", "B"),
        ("What does the `lm()` function in R do?", "Create a linear model", "Create a list", "Calculate the mean", "Calculate the sum", "A"),
        ("Which operator is used for assignment in R?", "<-", "=", "==", "->", "A"),
        ("What does the `summary()` function in R do?", "Summarizes a dataset", "Summarizes a plot", "Finds missing values", "Creates a dataframe", "A"),
        ("Which function is used to view the structure of an R object?", "str()", "view()", "summary()", "describe()", "A"),
        ("How do you generate a random number in R?", "random()", "rand()", "runif()", "rnorm()", "C"),
        ("Which function is used to combine two data frames by columns in R?", "cbind()", "merge()", "rbind()", "bind()", "A"),
    ],
    "DS3850": [
        ("What is the output of print(2 + 3 * 4)?", "14", "20", "12", "16", "A"),
        ("Which function is used to get the length of a list?", "size()", "len()", "length()", "count()", "B"),
        ("What does the 'def' keyword do in Python?", "Defines a class", "Defines a function", "Declares a variable", "Imports a module", "B"),
        ("Which of the following is a mutable data type?", "Tuple", "String", "List", "String", "C"),
        ("What does '== 'operator do in Python?", "Assigns a value", "Compares two values", "Adds two values", "Divides two values", "B"),
        ("How do you create a dictionary in Python?", "{}", "[]", "()", "<>", "A"),
        ("Which of the following is not a valid variable name?", "_variable", "variable1", "2variable", "variable_two", "C"),
        ("Which Python function is used to read input from the user?", "read()", "input()", "scan()", "get_input()", "B"),
        ("What is the result of 10 // 3?", "3", "3.0", "4", "3.333", "A"),
        ("What does the 'import' keyword do in Python?", "Imports a library", "Defines a function", "Declares a variable", "Runs the code", "A"),
    ],
    "DS3860": [
       ("What does SQL stand for?", "Structured Query Language", "Simple Query Language", "Standard Query Language", "System Query Language", "A"),
       ("Which of the following is used to retrieve data from a database?", "INSERT", "SELECT", "UPDATE", "DELETE", "B"),
       ("What is a primary key in a database?", "A unique identifier for a record", "A foreign identifier", "A non-unique field", "A table identifier", "A"),
       ("What does the 'JOIN' command do in SQL?", "Adds data to a table", "Combines rows from two or more tables", "Deletes records", "Creates a new table", "B"),
       ("Which of the following is a type of database relationship?", "One-to-one", "One-to-many", "Many-to-many", "All of the above", "D"),
       ("Which SQL command is used to modify existing records?", "INSERT", "UPDATE", "SELECT", "DELETE", "B"),
       ("What is a foreign key?", "A key in a child table that links to the primary key of the parent table", "A key that stores data values", "A key that stores passwords", "A key in a primary table", "A"),
       ("Which SQL clause is used to filter records?", "WHERE", "ORDER BY", "HAVING", "SELECT", "A"),
       ("What is normalization in database design?", "The process of organizing data to avoid redundancy", "The process of indexing data", "The process of combining tables", "The process of storing data in flat files", "A"),
       ("What is a relational database?", "A database that stores data in tables with relationships", "A database that stores data in files", "A database that uses no relationships", "A database without tables", "A")
    ],
}

# Insert sample data into each category table if empty
for category, questions in sample_data.items():
    table_name = category.lower().replace(' ', '_') + "_questions"  # Format the table name
    
    # Check if the table exists and create it if not
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            question_text TEXT,
            option_a TEXT,
            option_b TEXT,
            option_c TEXT,
            option_d TEXT,
            correct_answer TEXT
        )
    ''')

    # Insert the questions if the table is empty
again = input("You already ran this... you sure you want to do this again? Yes/No")

if again == "Yes":
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    if cursor.fetchone()[0] == 0:
        for question in questions:
            cursor.execute(f'''
            INSERT INTO {table_name} (question_text, option_a, option_b, option_c, option_d, correct_answer)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', question)
        conn.commit()

conn.close()
