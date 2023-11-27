from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime(num):
    result = {"Number": num, "isPrime": is_prime(num)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify

app = Flask(__name__)

airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
}

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    airport_info = airport_data.get(icao.upper())

    if airport_info:
        result = {"ICAO": icao.upper(), "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)