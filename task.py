from files import Files
from ldapservice import LDAPService
from dao import Dao

#read a csv
f = Files()
rows = f.readCSV('data.csv')
#print rows

#ldap dc=daf,dc=test,dc=it
#l = LDAPService("localhost","ldap","example","org", "admin")

d = Dao()
d.dropTable()
d.createTable()
print "Insert rows"
for i in rows:
    sentence = "INSERT INTO EMAIL (NAME,SUBJECT,EMAIL) VALUES ('{}','{}','{}')".format(i[0],i[1],i[2])
    print(sentence)
    d.execute(sentence)
