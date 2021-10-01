"""
Не думаю, что кто-то сюда полезет, поэтому никаким
PEP 8 здесь и не пахнет...
"""
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('first.html')


app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))