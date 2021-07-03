import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "masiandsepehr7368"
conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)


def create_user_database(userdata):
    cur = conn.cursor()
    cur.execute( """Insert into users(first_name,last_name,phone_number,birth_day,password_to_login,email) VALUES (%s, %s,%s,%s,%s,%s);""",(userdata['first_name'], userdata['last_name'], userdata['phone_number'], userdata['birthday'], userdata['password'],userdata['email']))
    conn.commit()
    cur.close()
def update_user_database(userdata):
    cur = conn.cursor()
    cur.execute("""UPDATE users SET "first_name" =%s,"last_name"=%s,"phone_number"=%s,"birth_day"=%s,"password_to_login"=%s,"email"=%s  WHERE phone_number =%s""",(userdata['first_name'], userdata['last_name'], userdata['phone_number'], userdata['birthday'], userdata['password'],userdata['email'],userdata['phone_number']))
    conn.commit()
    cur.close()
def delete_user_database(userdata):
    cur=conn.cursor()
    cur.execute("""DELETE FROM users WHERE "phone_nmumber"=%s""",(userdata['phone_number']));
    conn.commit()
    cur.close()


def read_user_database(phone_number='*'):
    cur = conn.cursor()
    if phone_number == "*":
        s = 'SELECT * FROM users'
    else:
        s = 'SELECT * From users where phone_number=%s'
    cur.execute(s, (phone_number,))
    list_users = cur.fetchall()
    cur.close()
    return list_users
