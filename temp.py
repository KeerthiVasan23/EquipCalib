import sqlite3
import datetime

conn=sqlite3.connect('equipment.db')
cur=conn.cursor()

cur.execute('SELECT * FROM equipment')
dbdata=cur.fetchall()
rows=len(dbdata)
i=0
now=str(datetime.date.today())
print (now)
while i<rows:
    if(now==dbdata[i][6]):
        print (dbdata[i][0],dbdata[i][1],dbdata[i][2],dbdata[i][3],dbdata[i][4],dbdata[i][5])
    i+=1 

