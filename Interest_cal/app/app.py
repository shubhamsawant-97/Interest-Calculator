from flask import Flask, render_template, Request
from flask.globals import request
from interest_cal import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("interest_cal.html")


@app.route("/", methods=["POST"])
def data():
    Amount = int(request.form["Amount"])
    Period_in_month = int(request.form["Period in month"])
    Rate_of_interest = float(request.form["Rate of interest"])
    Frequency = request.form["Period"]
    print(Frequency)
    if Frequency == "monthly":
        Interest = monthly(Amount, Rate_of_interest, Period_in_month)
    elif Frequency == "quaterly":
        Interest = quarterly(Amount, Rate_of_interest, Period_in_month)
    elif Frequency == "half_yearly":
        Interest = half_yearly(Amount, Rate_of_interest, Period_in_month)
    else:
        Interest = yearly(Amount, Rate_of_interest, Period_in_month)
    print(Interest)
    return render_template("interest_cal.html", i=Interest)


if __name__ == "__main__":
    app.run(debug=True)
