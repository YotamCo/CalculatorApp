from flask import Flask, render_template, request
from calculator import Calculator
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def calculate():
    form = request.form
    num1 = form.get("leftOperand")
    num2 = form.get("rightOperand")
    if num1 == "" or num2 == "":
        result = 'Missing operands'
        return render_template('index.html', calculationResult=result)
    if not num1.isnumeric() or not num2.isnumeric():
        result = 'Invalid operands'
        return render_template('index.html', calculationResult=result)
    operator = form.get("operator")
    calculator = Calculator()
    try:
        result = calculator.calculate(int(num1), int(num2), operator)
        result = "{:,}".format(result)
    except(ZeroDivisionError):
        result = 'Cannot divide by zero'
    return render_template('index.html', calculationResult=result)

if __name__ == '__main__':
    app.run(debug=True)