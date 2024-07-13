from flask import Flask,render_template 

app=Flask(__name__)
@app.route('/')
def index():
     return render_template('index.html')
@app.route("/welcome")
def welcome():
     return "welcome To Flask"
@app.route("/welcome")
def login():
     return render_template('login.html')
@app.route("/welcome")
def register():
     return render_template('register.html')

if __name__ =='__main__':
    app.run(debug=True)

