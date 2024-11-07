import sqlite3

def read_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_bowl.db')
    cursor = conn.cursor()
    
    # Fetch all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all table names
    print("Tables in the database:")
    for idx, table in enumerate(tables, start=1):
        print(f"{idx}. {table[0]}")
    
    # Prompt user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    if 0 <= table_index < len(tables):
        selected_table = tables[table_index][0]
        
        # Fetch and print data from the selected table
        cursor.execute(f"SELECT * FROM {selected_table};")
        rows = cursor.fetchall()
        
        print(f"\nData from table '{selected_table}':")
        for row in rows:
            print(row)
    else:
        print("Invalid selection.")
    
    # Close the database connection
    conn.close()

# Run the function
read_database()