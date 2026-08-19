import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

#Database
def init_db():
    conn = sqlite3.connect("calculator.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num1 REAL, 
            operation TEXT,
            num2 REAL,
            result TEXT
            )   
        """)

    conn.commit()
    conn.close()


init_db()

#cal fun

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

def floor(a, b):
    return a // b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

@app.route("/", methods=["GET", "POST"])
def home():
    result = None


    if request.method == "POST":
        try:

            a = float(request.form["num1"])
            b = float(request.form["num2"])

            operation = request.form["operation"]

            if operation == "add":
                result = add(a, b)

            elif operation == "subtract":
                result = subtract(a, b)

            elif operation == "multiply":
                result = multiply(a, b)

            elif operation == "divide":
                result = divide(a, b)

            elif operation == "floor":
                result = floor(a, b)

            elif operation == "modulus":
                result = modulus(a, b)

            elif operation == "exponent":
                result = exponent(a, b)

        except ValueError:
            result = "Please enter valid numbers"

        except ZeroDivisionError as e:
            result = e



        #save to database

        conn = sqlite3.connect("calculator.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO history(num1, operation, num2, result)
            VALUES(?, ?, ?, ?)
            """, (a, operation, b, str(result)))
        conn.commit()
        conn.close()
    return render_template("index.html", result = result)

@app.route("/history")
def history():
    conn = sqlite3.connect("calculator.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return render_template("history.html", rows=rows)


    

if __name__ == "__main__":
    app.run(debug=True)

