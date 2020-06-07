from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello():
    equation, answer = math_problem()
    return f"{equation} = ??"

def math_problem():
    lower_bound = 1
    upper_bound = 20
    a = random.randint(lower_bound, upper_bound)
    b = random.randint(lower_bound, upper_bound)
    operation = random.choice(['-', '+', '*', '/'])
    equation = f"{a} {operation} {b}"
    answer = eval(equation)
    return equation, answer

if __name__ == '__main__':
    app.run()