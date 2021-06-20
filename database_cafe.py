import psycopg2

conn = psycopg2.connect(database="cafe_project", user='postgres', password='mehdi2053', host='127.0.0.1', port='5432')

cursor = conn.cursor()
cursor.execute("")
conn.commit
# data = cursor.fetchone()

conn.close()
