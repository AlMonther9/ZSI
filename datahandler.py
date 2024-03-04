import sqlite3
import time
# # Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('data.db')

# # Create a cursor object to interact with the database
# cursor = conn.cursor()

# # Create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# # Insert some data into the table
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 35))

# # Commit the changes to the database
# conn.commit()

# # Query the data
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Close the connection
# conn.close()


class DataHandler:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('data.db')
        self.conn.row_factory = sqlite3.Row  # Access columns by name
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS test
                            (id INTEGER PRIMARY KEY, time INTEGER, gas INTEGER, bme INTEGER)''')


    def store_data(self, data: str) -> None:
    # Parse the data string to extract the individual values
        values = data.split(' ')
        if len(values) == 2:
            current_time = int(time.time())
            gas_value = int(values[0])
            bme_value = int(values[1])
            # Insert the data into the database
            with self.conn:
                self.cursor.execute("INSERT INTO test (time, gas, bme) VALUES (?, ?, ?)", (current_time, gas_value, bme_value))
        else:
            print("Invalid data format")

    def display_data(self) -> dict:
        with self.conn:
            self.cursor.execute("SELECT * FROM test")
            rows = self.cursor.fetchall()
            data = {}
            for row in rows:
                data[row[0]] = {
                    'time': row[1],
                    'gas': row[2],
                    'bme': row[3]
                }
            return data
