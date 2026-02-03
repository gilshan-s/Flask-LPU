from flask import Flask 
app=Flask(__name__)
@app.route("/")
def Test_Case1():
    return "<h1 style='color:blue;background-color:yellow;border-radius:15px'>Welcome to About Us Page</h1>"
@app.route("/home")
def Test_Case2():
    return "<h1 style='color:blue;background-color:yellow;border-radius:15px'>Welcome to Home Page</h1>"
@app.route("/services")
def Test_Case3():
    return "<h1 style='color:blue;background-color:yellow;border-radius:15px'>Welcome to Services Page</h1>"
@app.route("/contact")
def Test_Case4():
    return "<h1 style='color:blue;background-color:yellow;border-radius:15px'>Welcome to Contact Page</h1>"
if(__name__=="__main__"):
    app.run(debug=True)