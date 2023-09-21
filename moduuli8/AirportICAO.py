import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='data',
         user='root',
         password='salasana',
         autocommit=True
         )

icao = input("Anna lentokentän ICAO-koodi: ")

cursor = connection.cursor()
cursor.execute(f"SELECT ident, name, municipality FROM airports WHERE ident = '{icao}'")
results = cursor.fetchall()

for row in results:
    print(f"Lentokenttä: {row[1]}, Sijaintikunta: {row[2]}")

cursor.close()
connection.close()
