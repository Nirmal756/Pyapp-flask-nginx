import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Fetching the variable from .env via Docker environment
    branch = os.getenv('GIT_BRANCH', 'unknown')
    return render_template('index.html', branch=branch)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
