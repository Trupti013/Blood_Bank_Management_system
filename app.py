
from flask import *
from dbm import *

app =Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/blood")
def blood():
    return render_template("blood.html")





@app.route("/Dregistration")
def Dregistration():
    return render_template("Dregistration.html")

@app.route("/insert_donor",methods=["post"])
def insd():
    name=request.form["name"]
    dob=request.form["dob"]
    blood_group=request.form["blood_group"]
    last_donated=request.form["last_donated"]
    phone_no=request.form["phone_no"]
    email=request.form["email"]
    password=request.form["password"]
    area=request.form["area"]
    s=(name,dob,blood_group,last_donated, phone_no, email, password, area)
    insert_donor(s)
    return redirect("/Dend")

@app.route("/Dend")
def Dend():
    return render_template("Dend.html")

@app.route("/Dlogin")
def Dlogin():
    return render_template("Dlogin.html")

@app.route("/DLcheck", methods=["post"])
def DLcheck():
    global email_donor
    email_donor=request.form['email']
    global password_donor
    password_donor=request.form['password']
    global a
    a=(email_donor, password_donor)
    a1=DLlog_check(a)
    if a in a1:
        return redirect("/donors")
    else:
        return redirect("/Dlogin")


dc="select"
@app.route("/donors")
def donors():
    if dc=="select":
        d=Dselectuser2()
        return render_template("donors.html", x=d)
    else:
        a=Dselectuser(dc)
        return render_template("donors.html", x=a)

@app.route("/Dcheck", methods=["post"])
def Dcheck():
    blood_group=request.form['blood_group']
    global dc
    dc=blood_group
    return redirect("/donors")




@app.route("/doedit")
def doedt():
    a1=Dedituser(a)
    return render_template("doedit.html", x=a1)

@app.route("/doupdate", methods=["post"])
def doupd():
    name=request.form['name']
    dob=request.form['dob']
    blood_group=request.form["blood_group"]
    last_donated=request.form["last_donated"]
    phone_no=request.form["phone_no"]
    email=request.form['email']
    password=request.form['password']
    area=request.form["area"]
    t=(name,dob,blood_group,last_donated,phone_no,email,password,area,email_donor, password_donor)
    Dupdate(t)
    return redirect('/Dlogin')



@app.route("/dodelete")
def dell():
    Ddeleteuser(a)
    return redirect("/")






@app.route("/Rregistration")
def Rregistration():
    return render_template("Rregistration.html")

@app.route("/insert_recipient",methods=["post"])
def insr():
    name=request.form["name"]
    dob=request.form["dob"]
    blood_group=request.form["blood_group"]
    phone_no=request.form["phone_no"]
    email=request.form["email"]
    password=request.form["password"]
    area=request.form["area"]
    s=(name, dob, blood_group, phone_no, email, password, area)
    insert_recipient(s)
    return redirect("/Rend")

@app.route("/Rend")
def Rend():
    return render_template("Rend.html")





@app.route("/Rlogin")
def Rlogin():
    return render_template("Rlogin.html")

@app.route("/RLcheck", methods=["post"])
def RLcheck():
    global email_recipient
    email_recipient=request.form['email']
    global password_recipient
    password_recipient=request.form['password']
    global a
    a=(email_recipient, password_recipient)
    a1=RLlog_check(a)
    if a in a1:
        return redirect("/recipient")
    else:
        return redirect("/Rlogin")



rc="select"
@app.route("/recipient")
def recipient():
    if rc=="select":
        d=Rselectuser2()
        return render_template("recipient.html", x=d)
    else:
        a=Rselectuser(rc)
        return render_template("recipient.html", x=a)


@app.route("/Rcheck", methods=["post"])
def Rcheck():
    blood_group=request.form['blood_group']
    global rc
    rc=blood_group
    return redirect("/recipient")

@app.route("/reedit")
def redt():
    a1=Redituser(a)
    return render_template("reedit.html", x=a1)

@app.route("/reupdate", methods=["post"])
def reupd():
    name=request.form['name']
    dob=request.form['dob']
    blood_group=request.form["blood_group"]
    phone_no=request.form["phone_no"]
    email=request.form['email']
    password=request.form['password']
    area=request.form["area"]
    t=(name,dob,blood_group,phone_no,email,password,area,email_recipient, password_recipient)
    Rupdate(t)
    return redirect('/Rlogin')

@app.route("/redelete")
def redell():
    a=(email_recipient, password_recipient)
    Rdeleteuser(a)
    return redirect("/")



@app.route("/Alogin")
def Alogin():
    return render_template("Alogin.html")

@app.route("/ALcheck", methods=["post"])
def ALcheck():
    email=request.form['email']
    password=request.form['password']
    a=(email, password)
    a1= ALlog_check(email)
    if a in a1:
        return redirect("/Admin")
    else:
        return redirect("/")

@app.route("/Admin")
def Admin():
    return render_template("Admin.html")

@app.route('/Adonor')
def Adonor():
    a=Rselectuser2()
    return render_template('Adonor.html', x=a)

@app.route('/Arecipient')
def Arecipient():
    a=Dselectuser2()
    return render_template('Arecipient.html',x=a)


@app.route('/Dedit')
def Dedt():
    a=request.args.get('l')
    global a1
    a1= tuple(x for x in a.split(", ") )
    data=Dedituser(a1)
    return render_template('ADedit.html',x=data)

@app.route('/Dupdate',methods=['post'] )
def Dupd():
    name=request.form['name']
    dob=request.form['dob']
    blood_group=request.form["blood_group"]
    last_donated=request.form["last_donated"]
    phone_no=request.form["phone_no"]
    email=request.form['email']
    password=request.form['password']
    area=request.form["area"]
    t=(name,dob,blood_group,last_donated,phone_no,email,password,area,a1[0], a1[1])
    Dupdate(t)
    return redirect('/Adonor')

@app.route('/Ddelete')
def Ddell():
    a=request.args.get('l')
    a2= tuple(x for x in a.split(", ") )
    Ddeleteuser(a2)
    return redirect('/Adonor')

@app.route('/Redit')
def Redt():
    a=request.args.get('l')
    global a1
    a1= tuple(x for x in a.split(", ") )
    data=Redituser(a1)
    return render_template('ARedit.html',x=data)

@app.route('/Rupdate',methods=['post'] )
def Rupd():
    name=request.form['name']
    dob=request.form['dob']
    blood_group=request.form["blood_group"]
    phone_no=request.form["phone_no"]
    email=request.form['email']
    password=request.form['password']
    area=request.form["area"]
    t=(name,dob,blood_group,phone_no,email,password,area,a1[0], a1[1])
    Rupdate(t)
    return redirect('/Arecipient')

@app.route('/Rdelete')
def Rdell():
    a=request.args.get('l')
    a2= tuple(x for x in a.split(", ") )
    Rdeleteuser(a2)
    return redirect('/Arecipient')

if __name__=="__main__":
    app.run(debug="True")