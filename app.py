from flask import Flask, render_template, request, make_response, jsonify
import os
import json
app = Flask(__name__)

@app.route('/')
def information_details():
   data = {
   "Name":"Purvi patel",
   "Student :"200522745",
   "class":"Conversational Artificial intelligence"
      }
   return render_template('home.html', data=json.dumps(data, indent=4))
	
@app.route('/webhook', methods = ['POST'])
def order():
   return make_response(jsonify({'fulfillmentText': "Thank you for odering your pizza with us."}))

if __name__ == '__main__':
   app.run(debug = True)