import hashlib
import random
import MySQLdb
key = "my original activation key"
activation_key = []
saltlist = []
for i in range(1,21):  #generate 20 codes
    sha1 = hashlib.sha1()
    sha1.update(key.encode("utf-8"))
    salt = str(random.random())[:5]
    sha1.update(salt.encode("utf-8"))
    activation_key.append(sha1.hexdigest())
print(activation_key)

# connect to database
db = MySQLdb.connect("localhost","testuser","passwd","TESTDB")
cursor = db.cursor()
# create table
cursor.execute("DROP TABLE IF EXISTS ACTIVATIONKEY")
sql = """CREATE TABLE ACTIVATIONKEY (
         id INT Primary KEY AUTO_INCREMENT,
         mykey VARCHAR(100)) """
try:
    cursor.execute(sql)
except:
    print("Error: unable to create table")
    db.rollback()

# insert into database
for i in range(1,21):
    temp = """INSERT INTO ACTIVATIONKEY (id,mykey) VALUES ("""
    sql =temp+str(i)+","+"'"+activation_key[i-1]+"'"+");"

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error: unable to insert data")
        db.rollback()

# read database
sql = """SELECT * FROM ACTIVATIONKEY WHERE 1;"""

try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      dataid = row[0]
      keyvalue = row[1]
      print (str(dataid) + " : "+ keyvalue)
except:
   print("Error: unable to fecth data")
db.close()
