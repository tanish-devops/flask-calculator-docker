from flask import Flask, render_template, request

app = Flask(__name__)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = sub(num1, num2)
            elif operation == "*":
                result = mul(num1, num2)
            elif operation == "/":
                result = div(num1, num2)
        except ZeroDivisionError as e:
            error = str(e)
        except (ValueError, TypeError):
            error = "Please enter valid numbers."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,debug=True)
