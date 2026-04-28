import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get the variable, but provide a clear error message if it's missing
    branch = os.getenv('GIT_BRANCH', 'Variable Not Found')

    # Debug print: This will show up in 'docker logs <container_id>'
    print(f"DEBUG: Current branch variable is: {branch}")

    return render_template('index.html', branch=branch)
