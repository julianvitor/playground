from flask import Flask, jsonify

app = Flask(__name__)

# Contador de solicitações
request_count = 0

@app.route('/flask')
def index():
    global request_count
    request_count += 1
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
