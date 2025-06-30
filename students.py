import sqlite3
conn=sqlite3.connect("students.db")
print("database created succesfully")
conn.close()
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute("""
Create table if not exists students(
  id integer primary key,
  name text not null,
  age integer not null,
  grade text
)
""")
conn.commit()
conn.close()
conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("Insert into students (name,age,grade) values( ?,?,?)",("alice",34,"A"))
cursor.execute("Insert into students (name,age,grade) values( ?,?,?)",("nav",24,"B"))
cursor.execute("Insert into students (name,age,grade) values( ?,?,?)",("rahul",44,"F"))
cursor.execute("Insert into students (name,age,grade) values( ?,?,?)",("tarun",54,"B"))
cursor.execute("Insert into students (name,age,grade) values( ?,?,?)",("beeny",14,"A"))
conn.commit()
print("data inserted successfully")

# reterving the data
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute("select * from students")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()
import pandas as pd
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute("select * from students")
rows=cursor.fetchall()
df=pd.DataFrame(rows,columns=["id","name","age","grade"])
df.to_csv("students.csv",index=False)
print("CSV file created successfully")