import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

def create_table():
	query = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN)"
	cursor.execute(query)

def insert_values(value):
	query = "INSERT INTO todos VALUES (NULL, ?, 0)"
	cursor.execute(query, (value,))

def save_and_close_db():
	connection.commit() # Save changes to the database
	connection.close()

def main():
	create_table()
	user_input = input("Write in the todo name: ")
	insert_values(user_input)
	save_and_close_db()

if __name__ == '__main__':
	main()