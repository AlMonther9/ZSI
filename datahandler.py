import sqlite3
import time



class DataHandler:
    def __init__(self) -> None:
        pass


    def store_data(self, data: str) -> None:
    # Parse the data string to extract the individual values
        values = data.split(' ')
        if len(values) == 2:
            timeInSeconds = int(time.time())
            currentTime = time.ctime(timeInSeconds)
            gas_value = int(values[0])
            bme_value = int(values[1])
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO test (time, gas, bme) VALUES (?, ?, ?)", (currentTime, gas_value, bme_value))
            conn.commit()  
            conn.close()

        else:
            print("Invalid data format")

    def display_data(self) -> dict:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        rows = cursor.fetchall()
        data = {}
        for row in rows:
            data[row[0]] = {
                'time': row[1],
                'gas': row[2],
                'bme': row[3]
            }
        return data
