import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

def create_table():
	query = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN)"
	cursor.execute(query)

def display_todos():
	query = "SELECT * FROM todos"
	result = cursor.execute(query)
	for row in result:
		print(row)

def insert_todo(value):
	query = "INSERT INTO todos VALUES (NULL, ?, 0)"
	cursor.execute(query, (value,))

def check_if_todo_exists(todo_id):
	query = "SELECT count(id) FROM todos WHERE id = ?"
	cursor.execute(query, (todo_id,))
	data = cursor.fetchone()[0]
	return (data != 0)

def update_todo(new_name, todo_id):
	query = "UPDATE todos SET name = ? WHERE id = ?"
	cursor.execute(query, (new_name, todo_id))

def delete_todo(todo_id):
	query = "DELETE FROM todos WHERE id = ?"
	cursor.execute(query, (todo_id,))

def save_and_close_db():
	connection.commit() # Save changes to the database
	connection.close()

def main():
	create_table()

	active = True

	while active:
		user_input = input("Select option [ 1 - Display todos, 2 - Insert todo, 3 - Update todo, 4 - Delete todo, q - Exit ]:\n")
		if user_input == "1":
			display_todos()
		elif user_input == "2":
			new_todo = input("Enter new todo:\n")
			insert_todo(new_todo)
		elif user_input == "3":
			display_todos()
			selection_id = input("Enter ID you want to update:\n")
			if check_if_todo_exists(int(selection_id)):
				new_name = input("Enter updated todo:\n")
				update_todo(new_name, selection_id)
			else:
				print("Sorry, this ID doesn't exist!\n")
		elif user_input == "4":
			display_todos()
			selection_id = input("Enter ID you want to delete:\n")
			delete_todo(int(selection_id))
		else:
			active = False
			
	save_and_close_db()

if __name__ == '__main__':
	main()