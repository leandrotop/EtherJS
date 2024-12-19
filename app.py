from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'Index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
