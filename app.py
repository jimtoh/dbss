from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
# app must match app.py
# app match all other app

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html")) # to launch this index.html

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    q = float(request.form.get("q"))
    return(render_template("prediction.html",r=(-50.6*q)+90.2)) # run prediction.html

# r=(-50.6*q)+90.2) :: from 

if __name__ == "__main__":
    app.run()

# here for local testing