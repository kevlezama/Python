import psycopg2

USER = 'postgres'
PASS = 'admin'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'test_1_db'

conn = psycopg2.connect(user=USER, password=PASS, host=HOST, port=PORT, database=DB)
cursor = conn.cursor()
query = 'SELECT * FROM public.employees'
cursor.execute(query)
data = cursor.fetchone()
print(data)

cursor.close()
conn.close()