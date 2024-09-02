#flask,scikit-learn, pandas, pickle-mixin 

import pandas as pd 
from flask import Flask, render_template, requests

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, port=5001)