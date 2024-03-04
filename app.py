from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about_me.html")

@app.route("/yub")
def yub():
    return render_template("yub.html")
    
    
    
if __name__ == "__main__": app.run(host='0.0.0.0', port=5000,debug=True)

