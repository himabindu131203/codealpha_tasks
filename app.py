from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

def fibonacci(n):
    series = [0, 1]
    for _ in range(n - 2):
        series.append(series[-1] + series[-2])
    return series[:n]

@app.route('/fibonacci')
def get_fibonacci():
    num = int(request.args.get('num', 1))
    return jsonify(result=fibonacci(num))

if __name__ == '__main__':
    app.run(debug=True)
