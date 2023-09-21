import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='data',
         user='root',
         password='salasana',
         autocommit=True
         )

cursor = connection.cursor()
maa = input("Anna maakoodi: ")
cursor.execute(f"SELECT type, COUNT(type) FROM airports WHERE iso_country = '{maa}' GROUP BY type")
result = cursor.fetchall()

for row in result:
    airport_type = row[0]
    count = row[1]
    print(f"{airport_type}: {count} kappaletta")


cursor.close()
connection.close()