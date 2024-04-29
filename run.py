import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        # n.b. this MUST be false before submitting 
        # (security flaw, allows flawed code to be run )
        debug=True) 
    