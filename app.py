import sqlite3
import os.path
import time
from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
#something new
@app.route("/", methods=["POST", "GET"])
def home():
    if (request.method == "POST"):
        option = request.form.get("option")
        pollid = request.form.get("submit")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.cursor()
            if(option == "1"):
                db.execute("UPDATE pollcount set op1 = op1 + 1 where poll_id = :pollid",{"pollid":pollid})
            elif(option == "2"):
                db.execute("UPDATE pollcount set op2 = op2 + 1 where poll_id = :pollid", {"pollid": pollid})
            elif(option == "3"):
                db.execute("UPDATE pollcount set op3 = op3 + 1 where poll_id = :pollid", {"pollid": pollid})
            else:
                db.execute("UPDATE pollcount set op4 = op4 + 1 where poll_id = :pollid", {"pollid": pollid})
            database.commit()
        return redirect("/")
    else:
        return render_template("HomeNew.html")


@app.route("/dummyhome", methods=["POST", "GET"])
def dummyhome():
    if (request.method == "POST"):
        userid = session["id"]
        option = request.form.get("option")
        pollid = request.form.get("submit")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.cursor()
            if(option == "1"):
                db.execute("UPDATE pollcount set op1 = op1 + 1 where poll_id = :pollid",{"pollid":pollid})
            elif(option == "2"):
                db.execute("UPDATE pollcount set op2 = op2 + 1 where poll_id = :pollid", {"pollid": pollid})
            elif(option == "3"):
                db.execute("UPDATE pollcount set op3 = op3 + 1 where poll_id = :pollid", {"pollid": pollid})
            else:
                db.execute("UPDATE pollcount set op4 = op4 + 1 where poll_id = :pollid", {"pollid": pollid})
            database.commit()
            db = database.cursor()
            db.execute("INSERT INTO loginpollcount(poll_id, user_id)" " VALUES( :pollid, :userid)",
                       {"pollid": pollid, "userid": userid})
            database.commit()
        return redirect("/")
    else:
        return render_template("HomeNew.html")



@app.route("/logout", methods=["POST" , "GET"])
def logout():
    session["id"] = None
    session["username"] = None
    session["message"] = None
    session.clear()
    return redirect("/")

@app.route("/guest", methods=["POST" , "GET"])
def guest():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "polling.db")
    with sqlite3.connect(db_path) as database:
        db = database.execute("SELECT poll_id,ques FROM polldata")
        rows = db.fetchall()
        if len(rows) == 0:
            return render_template("text_generator.html", message="At present there are no polls")
        return render_template("guest_poll.html", arr=rows, l=len(rows))

@app.route("/loginportal", methods=["POST" , "GET"])
def loginportal():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "polling.db")
    with sqlite3.connect(db_path) as database:
        db = database.execute("SELECT poll_id,ques FROM polldata")
        rows = db.fetchall()
        if len(rows) == 0:
            return render_template("text_generator.html", message="At present there are no polls")
        print(len(session))
        if len(session) == 2:
            message = ""
        else:
            message = session["message"]
        return render_template("loginportal.html",arr=rows,l=len(rows),name=session["username"],msg=message)

@app.route("/loginpoll", methods=["POST", "GET"])
def loginpoll():
    print("LOgin Poll")
    if request.method == "POST":
        pollid = request.form.get("submit")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db = database.execute("SELECT * FROM polldata WHERE poll_id = :pollid ", {"pollid": pollid})
            row = db.fetchone()
            userid = session["id"]
            db = database.execute("SELECT * FROM loginpollcount WHERE poll_id = :pollid AND user_id = :userid",
                                  {"pollid": pollid , "userid" : userid})
            rows = db.fetchone()
            if(rows == None):
                return render_template("loginpollcast.html", question=row[2],op1=row[3],op2=row[4],op3=row[5],op4=row[6], poll_id=row[0])
            else:
                session["message"] = "Vote already registered for this user."
                return redirect("/loginportal")

    else:
        return render_template("text_generator.html", message="Error in Userpoll")


#check

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        #print("andar")
        username = request.form.get("uname")
        password = request.form.get("pass")
        otp = request.form.get("otp")
        if not username or not password:
            return ("\n Enter username and password")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.execute("SELECT * FROM user WHERE username = :username ",{"username":username})
            rows = db.fetchone()
            if rows == None or rows[2] != password or otp != OTP:
                return render_template("text_generator.html", message="Invalid Username or Password or OTP")
            # db = database.execute("SELECT poll_id,ques FROM polldata")
            # rows = db.fetchall()
            # return render_template("user_poll.html", arr=rows, l=len(rows))
            session.clear()
            session["id"] = rows[0]
            session["username"] = username
            return redirect("/loginportal")
    else:
        # print("bahar")
        return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("pass")
        confirm_password = request.form.get("cpass")

        if password != confirm_password:
            return render_template("text_generator.html", message="Passwords do not match")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")

        with sqlite3.connect(db_path) as database:
            db = database.execute("SELECT * FROM user WHERE username = :username ", {"username": username})
            rows = db.fetchone()
            if rows != None:
                return render_template("text_generator.html", message="Username Already Exists")
            db = database.cursor()
            db.execute("INSERT INTO user(username, password)" " VALUES( :username, :password)", {"username": username, "password": password})
            database.commit()

        return render_template("text_generator.html", message="Account Succesfully Created")
    else:
        return render_template("register.html")

@app.route("/temp", methods = ["POST", "GET"])
def temp():
    if request.method == "POST":
        # print("andar")
        return render_template("home.html")
    # print("bahar")
    return render_template("temp.html")

@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        #print("andar")
        username = request.form.get("uname")
        password = request.form.get("pass")
        # print(username)
        # print(password)
        if not username or not password:
            return ("\n Enter username and password")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db=database.execute("SELECT * FROM admin WHERE username = :username ",{"username":username})
            rows = db.fetchone()
            #print(generate_password_hash(password))
            if rows == None or rows[2] != password:
                return render_template("text_generator.html", message="Invalid username or password")
            session.clear()
            session["id"] = rows[0]
            session["username"] = username
            return render_template("adminportal.html", name=session["username"])
    else:
        # print("bahar")
        return render_template("AdminLogin.html")

@app.route("/polltype", methods=["POST"])
def polltype():
    if request.method == "POST":
        type = request.form.get("submit")
        #print(type)
        if(type == "1"):
            return redirect("/makepoll")
        else:
            return render_template("text_generator.html", message="Under maintenance")
    else:
        return render_template("text_generator.html", message="Error in PollType")

@app.route("/makepoll", methods=["POST", "GET"])
def makepoll():
    if not session.get("id"):
       return(render_template("AdminLogin.html"))

    if(request.method == "POST"):
        a_id = session.get("id")
        question = request.form.get("ques")
        option1 = request.form.get("op1")
        option2 = request.form.get("op2")
        option3 = request.form.get("op3")
        option4 = request.form.get("op4")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db = database.cursor()
            db.execute("INSERT INTO polldata(admin_id, ques, op1, op2, op3, op4)" 
                       " VALUES( :a_id, :question, :option1, :option2, :option3, :option4)",
                       {"a_id": a_id, "question": question, "option1":option1,"option2":option2,"option3":option3,
                        "option4":option4})
            db.execute("INSERT INTO pollcount(op1, op2, op3, op4)"
                       " VALUES( :option1, :option2, :option3, :option4)",
                       {"option1": 0, "option2": 0, "option3": 0,
                        "option4": 0})
            database.commit()
            return render_template("adminportal.html", name=session["username"], message="Poll Created Successfully")
    else:
        return render_template("makepoll.html")

@app.route("/guestpoll", methods=["POST"])
def guestpoll():
    if request.method == "POST":
        pollid = request.form.get("submit")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "polling.db")
        with sqlite3.connect(db_path) as database:
            db = database.execute("SELECT * FROM polldata WHERE poll_id = :pollid ", {"pollid": pollid})
            row = db.fetchone()
            return render_template("pollcast.html", question=row[2],op1=row[3],op2=row[4],op3=row[5],op4=row[6], poll_id=row[0])
    else:
        return render_template("text_generator.html", message="Error in Userpoll")

@app.route("/result", methods=["POST","GET"])
def result():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "polling.db")
    with sqlite3.connect(db_path) as database:
        db = database.cursor()
        db.execute("select * from polldata join pollcount using (poll_id)")
        rows = db.fetchall()
        if len(rows) == 0:
            return render_template("text_generator.html", message="No Polls yet")
        return render_template("result.html", arr=rows,l=len(rows))

