import os
import psycopg2

conn = psycopg2.connect(
	host = "threespacedb.ccw4zwitwgyp.us-east-1.rds.amazonaws.com",
	user= 'postgres',
	password= 'changeme',
	database = "postgres",
	port = '5432')

cur = conn.cursor()

conn.commit()

cur.close()
conn.close()	

