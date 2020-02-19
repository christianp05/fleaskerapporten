
from flask import Flask, render_template
import sqlite3 as sql

# set up a connection to the database of flæskesteg

#Get the 5 latest prices of flæskesteg

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	#GET THE PRICE OF THE LATES flæskesteg
	db = sql.connect("mydb")
	cursor = db.cursor()
	cursor.execute('''SELECT rema_pris, MAX(id) FROM priser''')
	sqlpris = cursor.fetchone()
	db.commit()
	
	return render_template("index.html", price=sqlpris[0])  # sets the html source
#runs the site on a local ip
if __name__ == "__main__":
    app.run('0.0.0.0')
