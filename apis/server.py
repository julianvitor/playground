from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/', methods=['GET', 'POST'])
def check_prime():
    result = None
    if request.method == 'POST':
        number = int(request.form['number'])
        if is_prime(number):
            result = f"{number} é um número primo."
        else:
            result = f"{number} não é um número primo."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
