
from datetime import date
import sqlite3 as sql
import requests
import json

#Open the json for price of flæskesteg
json_side = requests.get("https://3i8g24dm3n-dsn.algolia.net/1/indexes/aws-prod-products/401050?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.21.1&x-algolia-application-id=3I8G24DM3N&x-algolia-api-key=f692051765ea56d2c8a55537448fa3a2")

#Load the json content
parsed = json.loads(json_side.content)
pris = str(parsed["pricing"]["price"])
#get the time
time = date.today()

#Set up a database
db = sql.connect("mydb")
cursor = db.cursor()

#Insert the data to the database
cursor.execute('''INSERT INTO priser(rema_pris, time) VALUES(:pris, :time)''', {'pris':pris, 'time':time})
db.commit()

#See what data was inserted
cursor.execute('''SELECT rema_pris, MAX(id) FROM priser''')
#cursor.execute('''UPDATE priser SET rema_pris = NULL''')
sqlpris = cursor.fetchone()
print ("saved todays price: " + str(sqlpris[0]))
print ("this prices date was: " + str(time))
print(pris)
db.close
