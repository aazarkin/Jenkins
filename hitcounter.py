from flask import Flask, jsonify
import os
import threading

app = Flask(__name__)

# File to persist the counter
COUNTER_FILE = "/data/access_count.txt"

# Ensure the file exists
os.makedirs("/data", exist_ok=True)
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("0")

# Thread lock to avoid race conditions
lock = threading.Lock()

def read_counter():
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def write_counter(count):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))

@app.route('/')
def count_access():
    with lock:
        count = read_counter()
        count += 1
        write_counter(count)
    return jsonify({"message": "SANDBOX dashboard accessed", "count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
