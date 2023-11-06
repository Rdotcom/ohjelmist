from flask import Flask, request

app = Flask(__name__)


def isprime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


@app.route("/alkuluku/<int:number>", methods=["GET"])
def alkuluku(number):
    result = isprime(number)
    respond = {"Number": number, "isPrime": result}
    return respond

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)