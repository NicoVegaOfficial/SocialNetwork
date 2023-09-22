import pymysql
import security
import re

conn = pymysql.connect(
        host='localhost',
        user='nico', 
        password = "tobyX?890",
        db='circleconnect'
    )

def valid_user(user, password):
    users_list = []
    users_list.append((user))
    cur = conn.cursor()    
    sql = "select salt from users where username = %s and enabled = 1;"
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
            return True
        

def get_user_id(user):
    users_list2 = []
    users_list2.append((user))
    sql = "select id from users where username = %s;"
    cur = conn.cursor()
    cur.executemany(sql, users_list2)
    output = cur.fetchone()
    return output    

def add_user(user, email, password):
    format = r'^[a-zA-Z0-9]+$'
    if re.match(format, user):
        user_list = []
        user_list.append((user, email))
        cur = conn.cursor()    
        sql = "select username from users where username = %s or email = %s;"
        cur.executemany(sql, user_list)
        resultado = cur.fetchone()
        if(not resultado):
            r = security.random_salt()
            i = security.securepwd(r + password + r)
            users_list = []
            users_list.append((user, email, i, r))
            cur = conn.cursor()
            sql = "INSERT INTO users (username, email, passwd, salt, dateuser, enabled) VALUES (%s, %s, %s, %s, now(), 1);"
            x = cur.executemany(sql, users_list)
            conn.commit()
            if(x):
                return True

def change_password(user, password, new_password):
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
            return True

def search_user(name):
    cur = conn.cursor()    
    sql = "select username, email, dateuser from users where username = %s;"
    val = []
    val.append((name))
    cur.executemany(sql, val)
    output = cur.fetchone()
    return output

def post_up(access_id, contenido):
    userid = id_session(access_id)
    if(userid):
        cur = conn.cursor()
        sql = "insert into post (iduser, contenido, datepost) values (%s, %s,  now());"
        val2 = []
        val2.append((userid, contenido))
        cur.executemany(sql, val2)
        conn.commit()
        return True



def get_all_post():
    cur = conn.cursor()
    sql = "select username, contenido, datepost from post inner join users on post.iduser = users.id;"
    cur.execute(sql)
    return cur.fetchall()

def get_post(userid):
    val = []
    val.append((userid))
    cur = conn.cursor()
    sql = "select id from users where id = %s"
    cur.executemany(sql, val)
    x = cur.fetchone()
    if(x):
        sql = "select username, contenido, datepost from post inner join users on post.iduser = users.id where iduser =  %s;"
        val2 = []
        val2.append((userid))
        cur.executemany(sql, val2)
        return cur.fetchall()


def delete_post(idpost):
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
        if (cur):
            return True

def active_session(id_session, id_user):
    val = []
    val.append((id_session, id_user))
    cur = conn.cursor()
    sql = "insert into sessions (id_session, id_user, date_session) values (%s, %s, now())"
    cur.executemany(sql, val)
    conn.commit()

def id_session(session_id):
    cur = conn.cursor()    
    sql = "select id_user from sessions where id_session = %s;"
    val = []
    val.append((session_id))
    cur.execute(sql, val)
    output = cur.fetchone()
    if (output):
        return output
