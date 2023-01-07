import sqlite3

connection = sqlite3.connect('../DBase/PriceList/alumark_s44.db')

cursor = connection.cursor()

# Display columns
print('\nColumns in EMPLOYEE table:')
data = cursor.execute('''SELECT * FROM alumark_s44''')
for column in data.description:
    print(column[0])

# Display data
print('\nData in EMPLOYEE table:')
data = cursor.execute('''SELECT art, name FROM alumark_s44''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()

# Closing the connection
connection.close()