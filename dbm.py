import pymysql as p

def connect():
    return p.connect(host="localhost", user="root", password='oracle',database="trupti", port=3306)


def insert_donor(s):
    con=connect()
    cur=con.cursor()
    sql="insert into donor_register values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,s)
    con.commit()
    con.close()

def insert_recipient(s):
    con=connect()
    cur=con.cursor()
    sql="insert into recipient_register values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,s)
    con.commit()
    con.close()

def log_check(blood_group):
    con=connect()
    cur=con.cursor()
    sql="select * from recipient_register where blood_group=%s"
    cur.execute(sql, blood_group)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def DLlog_check(a):
    con=connect()
    cur=con.cursor()
    sql="select email, password from donor_register where email=%s and password=%s"
    cur.execute(sql, a)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def ALlog_check(z):
    con=connect()
    cur=con.cursor()
    sql="select email, password from admin where email=%s"
    cur.execute(sql, z)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def Dselectuser(c):
    con=connect()
    cur=con.cursor()
    sql='select * from recipient_register where blood_group=%s'
    cur.execute(sql, c)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def Dselectuser2():
    con=connect()
    cur=con.cursor()
    sql='select * from recipient_register;'
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def RLlog_check(a):
    con=connect()
    cur=con.cursor()
    sql="select email, password from recipient_register where email=%s and password=%s"
    cur.execute(sql, a)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def Rselectuser(c):
    con=connect()
    cur=con.cursor()
    sql='select * from donor_register where blood_group=%s'
    cur.execute(sql, c)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def Rselectuser2():
    con=connect()
    cur=con.cursor()
    sql='select * from donor_register'
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def Dedituser(a):
    con=connect()
    cur=con.cursor()
    sql='select * from donor_register where email=%s and password=%s'
    cur.execute(sql,a)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0]

def Dupdate(t):
    con=connect()
    cur=con.cursor()
    sql='update donor_register set name=%s, dob=%s, blood_group=%s,last_donated=%s, phone_no=%s, email=%s, password=%s, area=%s where email=%s and password=%s'
    cur.execute(sql,t)
    con.commit()
    con.close()

def Ddeleteuser(a):
    con=connect()
    cur=con.cursor()
    sql='delete from donor_register where email=%s and password=%s'
    cur.execute(sql,a)
    con.commit()
    con.close()

def Redituser(a):
    con=connect()
    cur=con.cursor()
    sql='select * from recipient_register where email=%s and password=%s'
    cur.execute(sql,a)
    data=cur.fetchall()
    print(data)
    con.commit()
    con.close()
    return data[0]

def Rupdate(t):
    con=connect()
    cur=con.cursor()
    sql='update recipient_register set name=%s, dob=%s, blood_group=%s, phone_no=%s, email=%s, password=%s, area=%s where email=%s and password=%s'
    cur.execute(sql,t)
    con.commit()
    con.close()

def Rdeleteuser(email):
    con=connect()
    cur=con.cursor()
    sql='delete from recipient_register where email=%s and password=%s'
    cur.execute(sql,email)
    con.commit()
    con.close()
