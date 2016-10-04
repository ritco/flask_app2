from flask import Flask, render_template, request
from flask.ext.SQLAlchemy import SQLAlchemy

app=Flask(__name__)
app.config(['SQLALCHEMY_DATABASE_URI']='postgres://ezdmyllpclxunr:KhN3kS0l_uTj9XXoJtxZpq44eV@ec2-54-228-196-12.eu-west-1.compute.amazonaws.com:5432/d1nqs704ta1tcm')
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_)
        self.em xxxxxxxxxxxxxxxxxxxxxxx

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'] )
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
