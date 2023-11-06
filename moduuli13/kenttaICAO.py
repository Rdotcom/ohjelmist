from flask import Flask, request, jsonify
import csv

app = Flask(__name__)
database = {}
# airports.csv moduuli13 kansiossa
with open('airports.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        icao = row["ident"]
        name = row["name"]
        municipality = row["municipality"]
        database[icao] = {'ICAO': icao, 'Name': name, 'Municipality': municipality}

@app.route("/kenttä/<string:icao>", methods=["GET"])
def airportinfo(icao):
    if icao in database:
        airport_info = database[icao]
        return jsonify(airport_info)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"})

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
