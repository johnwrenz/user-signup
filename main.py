from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
   #storage for error messages
    username_error = "" 
    password_error =""
    verify_error =""
    email_error =""
        
    if username =="" or " " in username:
        username_error = "invalid username"

    if password =="" or " " in password or len(password)<3 or len(password)>20:
        password_error = "invalid password"    

    if verify =="" or verify != password:
        password_error = "invalid verification"

    if email_error == "" and username_error =="" and verify_error =="" and password_error =="":
        return render_template("welcome.html", username = username)
    else:
        return render_template("index.html", username_error = username_error
                                         ,password_error = password_error
                                         ,verify_error = verify_error
                                         ,email_error = email_error
                                         ,username = username
                                         ,email = email)

@app.route("/")
def index():
    return render_template("index.html")
 

app.run()



