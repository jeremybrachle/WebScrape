# CSE 5341: Senior Design at SMU, Spring 2019
# Adam Ashcraft, Chase Goehring, Jeremy Brachle, Matthew Wagner, Nora Potenti
# this program will scrape the car data from platinum motor's website
# and turn into JSON so that our mobile app can read the data.
# this program will eventually run on a serve so that our app can
# call the API endpoint at any time

# import necessary libraries
import flask
from flask import jsonify
from flask_cors import CORS
# import the web scraping file
import pmScrape

# initialize the app and set up CORS
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

# api routes
# default
@app.route('/', methods=['GET'])
def home():
    return "Default Route"

# return car data as JSON
@app.route('/cars', methods=['GET'])
def api_all():
    jsonCars = pmScrape.getSoup()
    return jsonify(jsonCars)

# run the API
app.run()
