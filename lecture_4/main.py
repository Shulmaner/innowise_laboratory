# create_database.py
import sqlite3
import os


def create_database():
    # Remove existing database if it exists
    if os.path.exists('school.db'):
        os.remove('school.db')

    # Connect to the database
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    # Read and execute the SQL file
    with open('school_queries.sql', 'r') as sql_file:
        sql_commands = sql_file.read()

    # Split the SQL commands by semicolon and execute each one
    commands = sql_commands.split(';')
    for command in commands:
        if command.strip():
            try:
                cursor.execute(command)
            except sqlite3.Error as e:
                print(f"Error executing command: {e}")
                print(f"Command: {command[:100]}...")

    # Commit changes and close connection
    conn.commit()

    # Print results of each query
    print("=" * 60)
    print("DATABASE CREATED SUCCESSFULLY")
    print("=" * 60)

    # Execute and display each query result
    queries = {
        "3. All grades for Alice Johnson": """
        SELECT s.full_name, g.subject, g.grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        WHERE s.full_name = 'Alice Johnson'
        """,

        "4. Average grade per student": """
        SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) as average_grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        GROUP BY s.id, s.full_name
        ORDER BY average_grade DESC
        """,

        "5. Students born after 2004": """
        SELECT id, full_name, birth_year
        FROM students
        WHERE birth_year > 2004
        ORDER BY birth_year
        """,

        "6. Subjects and their average grades": """
        SELECT subject, ROUND(AVG(grade), 2) as average_grade
        FROM grades
        GROUP BY subject
        ORDER BY average_grade DESC
        """,

        "7. Top 3 students with highest average grades": """
        SELECT s.id, s.full_name, ROUND(AVG(g.grade), 2) as average_grade
        FROM students s
        JOIN grades g ON s.id = g.student_id
        GROUP BY s.id, s.full_name
        ORDER BY average_grade DESC
        LIMIT 3
        """,

        "8. Students who scored below 80 in any subject": """
        SELECT DISTINCT s.id, s.full_name
        FROM students s
        JOIN grades g ON s.id = g.student_id
        WHERE g.grade < 80
        ORDER BY s.id
        """
    }

    for title, query in queries.items():
        print(f"\n{title}")
        print("-" * 40)
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No results found")
        else:
            for row in results:
                print(row)

    # Show all tables
    print("\n" + "=" * 60)
    print("DATABASE TABLES AND STRUCTURE")
    print("=" * 60)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        print(f"\nTable: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  {col[1]} ({col[2]})")

    # Show indexes
    print("\n" + "=" * 60)
    print("DATABASE INDEXES")
    print("=" * 60)
    cursor.execute("SELECT name, tbl_name, sql FROM sqlite_master WHERE type='index';")
    indexes = cursor.fetchall()
    for idx in indexes:
        print(f"Index: {idx[0]} on table {idx[1]}")

    conn.close()
    print(f"\nDatabase saved as: school.db")
    print(f"SQL queries saved as: school_queries.sql")


if __name__ == "__main__":
    create_database()