import csv
import sqlite3

#Path to csv and database file
csv_file = 'D:/User_Data/User_Data.csv'
db_file = 'D:/User_Data/data.db'

#Create connection
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

#Table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    estimated_salary INTEGER,
    purchased INTEGER
)
'''
cursor.execute(create_table_query)
conn.commit()

# Read data from the CSV file and insert it into the database
with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        user_id = row['User ID']
        gender = row['Gender']
        age = row['Age']
        estimated_salary = row['EstimatedSalary']
        purchased = row['Purchased']

        # Insert the data in database
        insert_query = '''
        INSERT INTO users (user_id, gender, age, estimated_salary, purchased)
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (user_id, gender, age, estimated_salary, purchased))

# Commit changes and close database connection
conn.commit()
conn.close()

print("Data has been inserted into the SQLite database.")
