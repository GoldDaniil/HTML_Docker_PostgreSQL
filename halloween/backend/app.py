from flask import Flask, send_from_directory
import os

app = Flask(__name__)

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend')

@app.route('/')
def home():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/about')
def about():
    return send_from_directory(FRONTEND_DIR, 'about.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
