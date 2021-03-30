
from flask import Flask, jsonify, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

app = Flask(__name__)


@app.route("/")
def welcome():
    mars_db = db.mars_db.find()
    return render_template("index.html", dict = mars_db)


@app.route("/scrape")
def scraper():
    mars_db = db.mars_db
    mars_data = scrape_mars.scrape()
    mars_db.update({}, mars_data, upsert=True)
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)