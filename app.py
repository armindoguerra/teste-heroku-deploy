import os
from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')#, title='Home', user=user)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)