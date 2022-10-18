from flask import Flask, redirect,url_for
import pandas as pd
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Shekar, How are you doing??"

@app.route('/Fatty/<int:weight>')
def fatty(weight):
    return "You are Fatty Shekar, over 60 KG's. You've to loss"+str(weight-60)

@app.route('/slim/<int:weight>')
def slim(weight):
    return "You are slim Shekar, great"

@app.route('/results/<int:KGS>')
def results(KGS):
    result=""
    if KGS<60:
        result = "slim"
    else:
        result = "fatty"
    return redirect(url_for(result, weight=KGS))

if __name__=="__main__":
    app.run(debug=True)