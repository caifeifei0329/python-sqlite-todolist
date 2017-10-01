import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

def create_table():
	query = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN)"
	cursor.execute(query)

def insert_todo(value):
	query = "INSERT INTO todos VALUES (NULL, ?, 0)"
	cursor.execute(query, (value,))

def display_todos():
	query = "SELECT * FROM todos"
	result = cursor.execute(query)
	for row in result:
		print(row)

def save_and_close_db():
	connection.commit() # Save changes to the database
	connection.close()

def main():
	create_table()
	# user_input = input("Write in the todo name: ")
	# insert_todos(user_input)
	display_todos()
	save_and_close_db()

if __name__ == '__main__':
	main()