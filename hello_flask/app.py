import os
import smtplib
from flask import Flask, render_template, request, redirect
from flask_mail import Mail

app = Flask(__name__)

#Registered names
names = []

@app.route('/')
def index():
    return render_template("basketball.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", names=names)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    team = request.form.get("team")
    email = request.form.get("email")

    if not name or not team or not email:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('billykim618@gmail.com', 'itifgftmgzgljsnn')
    server.sendmail("billykim618@gmail.com", email, message)
    # names.append(f"{name} from {team}")
    # return redirect("/registrants")
    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
