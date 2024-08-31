from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)
status = "Initializing..."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def get_status():
    global status
    return jsonify({"status": status})

def run_server():
    app.run(debug=True, use_reloader=False, port=5000)

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
