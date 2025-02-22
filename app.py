import os
import subprocess
from flask import Flask
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your actual full name
    full_name = "John Doe"  

    # Attempt to get the system username
    username = getpass.getuser()

    # Get current time in IST (Asia/Kolkata)
    server_time_ist = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")

    # Run 'top' in batch mode (-b) for a single iteration (-n 1)
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    # Return a simple HTML page
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
    # Run on port 8080 by default
    app.run(host='0.0.0.0', port=8080)
