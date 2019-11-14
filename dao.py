#import MySQLdb
import mysql.connector

class Dao:

   serverName = "172.17.0.1"
   serverUser = "root"
   serverPassword = "root"
   serverDb = "meli"
   
   def __init__(self):
      print("Calling data access layer")

   def execute(self, sql):
      try:

         config = {
            'user': Dao.serverUser,
            'password': Dao.serverPassword,
            'host': Dao.serverName,
            'database': Dao.serverDb
         }

         # Open database connection
         cnx = mysql.connector.connect(**config)

         # prepare a cursor object using cursor() method
         cursor = cnx.cursor()

         cursor.execute(sql)

         cnx.commit()
         
         # disconnect from server
         cnx.close()

         return True

      except mysql.connector.Error as err:
         print(err)

   def createTable(self):
       # Create table as per requirement
      self.execute("CREATE TABLE EMAIL (NAME  VARCHAR(200) NULL, SUBJECT  VARCHAR(200) NULL, EMAIL VARCHAR(300) )")
   
   def dropTable(self):
      # Create table as per requirement
      self.execute("DROP TABLE IF EXISTS EMAIL")
        