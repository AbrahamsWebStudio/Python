#We Just Getting STVRT3D!
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="30/Oct.db!MySQL.2025")

mycursor = mydb.cursor()

mycursor.execute("Select * from genixdb.stvrt3d")


for iE in mycursor:
    print(f"This is the answer to the expression:{iE}")
