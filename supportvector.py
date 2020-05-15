import mysql.connector as MySQL80
class Mydb():
    def conn(self):
        db = MySQL80.connect(
        host= "localhost",
        port= "3306",
        user="root",
        passwd="zzzz",
        database = "emlak"
        )
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM emlak.11 WHERE Id=10660458" )
        print(mycursor.fetchall())


    def printt(self):
        print("deneme")
