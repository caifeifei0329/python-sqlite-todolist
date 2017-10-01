import sqlite3

connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

def create_table():
	query = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, name TEXT, status BOOLEAN)"
	cursor.execute(query)

def enter_data():
	query = "INSERT INTO todos VALUES (NULL, ?, 0)"
	values = [("69th Lesson",),
			  ("70th Lesson",),
			  ("71st Lesson",),
			  ("72nd Lesson",),
			  ("73rd Lesson",),
			  ("74th Lesson",)
			 ]
	cursor.executemany(query, values)

def save_and_close_db():
	connection.commit() # Save changes to the database
	connection.close()

def main():
	create_table()
	enter_data()
	save_and_close_db()

if __name__ == '__main__':
	main()