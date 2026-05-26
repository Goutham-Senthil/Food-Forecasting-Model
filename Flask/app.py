import os
import pickle
from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'fdemand.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return render_template("homepage.html")

@app.route('/home')
def home():
    return render_template("homepage.html")

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        p = 1 if request.form["hp"] == 'y' else 0
        q = 1  if request.form["pr"] == 'y' else 0
        r = float(request.form["op"])
        s = int(request.form["cu"])

        t = int(request.form["ccode"])
        u = int(request.form["rcode"])
        v = request.form["cat"]
        vlookup  ={
            'Beverages':0,
            'Biryani':1,
            'Dessert':2,
            'Extras':3,
            'Fish':4,
            'Other Snacks':5,
            'Pasta':6,
            'Pizza':7,
            'Rice Bowl':8,
            'Salad':9,
            'Sandwich':10,
            'Seafood':11,
            'Soup':12,
            'Starters':13
        }
        v = vlookup[v]
        
        w = [t,u,r,v,s,q,p]
        output = model.predict(w)
        print(output)
        
        return render_template("index.html",y="The predicted number of orders is "+str(output[0]))

# @app.route('/user')
# def User():
#     return 'Hello user!!'
if __name__ == "__main__":
    app.run(debug=True)
