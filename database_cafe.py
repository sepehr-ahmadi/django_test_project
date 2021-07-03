import psycopg2

DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "masiandsepehr7368"
conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)


def read_user_database():
    cur = conn.cursor()
    s = 'SELECT * FROM users'
    cur.execute(s)
    list_users = cur.fetchall()
    cur.close()
    return list_users
