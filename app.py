import os
import subprocess
from flask import Flask
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/')
def index():
    # Returns a greeting message on the main URL
    return "<h1>Hello, welcome to my Codespace app!</h1>"

@app.route('/htop')
def htop():
    full_name = "Linga Nithin"  # Replace with your actual full name
    username = getpass.getuser()
    server_time_ist = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    return f"""
    <html>
    <head><title>/htop Endpoint</title></head>
    <body>
      <h1>/htop Endpoint</h1>
      <p><strong>Name:</strong> {full_name}</p>
      <p><strong>Username:</strong> {username}</p>
      <p><strong>Server Time (IST):</strong> {server_time_ist}</p>
      <hr/>
      <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Listen on all interfaces at port 8080
    app.run(host='0.0.0.0', port=8080)
