import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password='password', host='127.0.0.1')
cursor = conn.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("Connection established to: ", data)
conn.close()
