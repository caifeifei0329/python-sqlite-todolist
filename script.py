import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

def create_table():
	query = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN)"
	cursor.execute(query)

def save_and_close_db():
	connection.commit() # Save changes to the database
	connection.close()

def main():
	create_table()
	save_and_close_db()

if __name__ == '__main__':
	main()