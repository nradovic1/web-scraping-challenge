from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():
    mars_data = mongo.db.mission_to_mars.find_one()

    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    final_dict= scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mission_to_mars.update({}, final_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)