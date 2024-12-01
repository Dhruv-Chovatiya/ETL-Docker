import pandas as pd
import mysql.connector

# Extract: Load data from CSV
data = pd.read_csv('../data/sample_data.csv')

# Transform: Example transformation - Convert city names to uppercase
data['city'] = data['city'].str.upper()

# Load: Insert transformed data into MySQL
connection = mysql.connector.connect(
    host="mysql_container",
    user="root",
    password="root",
    database="etl_db"
)

cursor = connection.cursor()

for index, row in data.iterrows():
    sql = "INSERT INTO people (id, name, age, city) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, tuple(row))

connection.commit()
cursor.close()
connection.close()
print("Data loaded successfully.")
