from flask import Flask,render_template,request, redirect, url_for

app = Flask(__name__)

import pickle
model = pickle.load(open(r'C:/Users/zains/Flask/fdemand.pkl','rb'))
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
        p = request.form["hp"]
        p = 1 if p=='y' else 0
        q = request.form["pr"]
        q = 1 if q=='y' else 0
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
        #print(p)
        return render_template("index.html",y=p)

# @app.route('/user')
# def User():
#     return 'Hello user!!'
if __name__ == "__main__":
    app.run(debug=True)
