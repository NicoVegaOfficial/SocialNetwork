import pymysql
import security
import re

conn = pymysql.connect(
        host='localhost',
        user='nico', 
        password = "",
        db='nebula'
    )

def valid_user(user, password):
    users_list = []
    users_list.append((user))
    valid = False
    cur = conn.cursor()    
    sql = "select salt from users where username = %s;"
    cur.executemany(sql, users_list)
    resultado = cur.fetchone()
    if(resultado):
        users_list2 = []
        x = security.securepwd(resultado[0] + password + resultado[0])
        users_list2.append((user, x))
        sql = "select * from users where username = %s and passwd = %s;"
        cur.executemany(sql, users_list2)
        output = cur.fetchone()
        if(output):
            sql = "select id from users where username = %s;"
            valid_user3 = []
            valid_user3.append(user)
            cur.executemany(sql, valid_user3)
            z = cur.fetchone()
            #active_session(z[0])
            valid = True
    return valid
        
def add_user(user, password):
    valid = False
    format = r'^[a-zA-Z0-9]+$'
    if re.match(format, user):
        user_list = []
        user_list.append((user))
        cur = conn.cursor()    
        sql = "select username from users where username = %s;"
        cur.executemany(sql, user_list)
        resultado = cur.fetchone()
        if(not resultado):
            r = security.random_salt()
            i = security.securepwd(r + password + r)
            users_list = []
            users_list.append((user, i, r))
            cur = conn.cursor()
            sql = "INSERT INTO users (username, passwd, salt, dateuser) VALUES (%s, %s, %s, now());"
            x = cur.executemany(sql, users_list)
            conn.commit()
            if(x):
                valid = True
    return valid

def change_password(user, password, new_password):
    valid = False
    cur = conn.cursor()    
    users_list = []
    users_list.append((user))
    sql = "select salt from users where username = %s;"
    cur.executemany(sql, users_list)
    resultado = cur.fetchone()
    if(resultado):
        r = security.random_salt()
        newpass = security.securepwd(r + new_password + r)
        oldpass = security.securepwd(resultado[0] + password + resultado[0])
        sql = "update users set passwd = %s where passwd = %s;"
        password_list = []
        password_list.append((newpass, oldpass))
        x = cur.executemany(sql, password_list)
        password_list2 = []
        password_list2.append((r, resultado[0]))
        sql2 = "update users set salt = %s where salt = %s;"
        y = cur.executemany(sql2, password_list2)
        conn.commit()
        if(x and y):
            valid = True            
    return valid

def search_user(name):
    cur = conn.cursor()    
    sql_name = "select username from users where username = %s;"
    sql_date = "select dateuser from users where username = %s;"
    val = []
    val.append((name))
    cur.executemany(sql_name, val)
    resultado_name = cur.fetchone()
    cur.execute(sql_date, val)
    resultado_date = cur.fetchone()
    x = {
            "Nombre": resultado_name[0],
            "fecha_registro": str(resultado_date[0])
        }
    return x

def post_up(userid, contenido):
    val = []
    val.append((userid))
    cur = conn.cursor()
    sql = "select id from users where id = %s;"
    cur.executemany(sql, val)
    x = cur.fetchone()
    if(x):
        sql = "insert into post (iduser, contenido, datepost) values (%s, %s,  now());"
        val2 = []
        val2.append((userid, contenido))
        cur.executemany(sql, val2)
        conn.commit()
    return True

def get_post(userid):
    output = None
    val = []
    val.append((userid))
    cur = conn.cursor()
    sql = "select id from users where id = %s"
    cur.executemany(sql, val)
    x = cur.fetchone()
    if(x):
        sql = "select contenido from post inner join users on post.iduser = users.id where iduser = %s;"
        val2 = []
        val2.append((userid))
        cur.executemany(sql, val2)
        output = cur.fetchall()
    return output

def delete_post(idpost):
    output = None
    val = []
    val.append((idpost))
    cur = conn.cursor()
    sql = "select idpost from post where idpost = %s;"
    cur.executemany(sql, val)
    x = cur.fetchone()
    if(x):
        sql = "DELETE FROM post WHERE idpost=%s;"
        val2 = []
        val2.append((idpost))
        cur.execute(sql, val)
        conn.commit()
    return output

def active_session(userid):
    val = []
    val.append(str(userid))
    cur = conn.cursor()
    sql = "insert into activeSessions (iduser, timesession) values (%s, now());"
    cur.executemany(sql, val)
    conn.commit()