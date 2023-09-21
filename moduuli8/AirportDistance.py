import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='data',
         user='root',
         password='salasana',
         autocommit=True
         )

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

cursor = connection.cursor()
cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airports WHERE ident = '{icao1}'")
result1 = cursor.fetchone()

cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airports WHERE ident = '{icao2}'")
result2 = cursor.fetchone()

if result1 and result2:
    coordinates1 = result1[0], result1[1]
    coordinates2 = result2[0], result2[1]
    distance = geodesic(coordinates1, coordinates2).kilometers
    print(f"Etäisyys {icao1} ja {icao2} välillä on {distance:.2f} km")

cursor.close()
connection.close()