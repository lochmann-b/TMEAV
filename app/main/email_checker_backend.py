
import os

import datetime

from flask import Flask, jsonify, request, render_template, abort
from app.email_utils import is_email_address_valid

from app.customers_xml_parser import check_email_addresses

#configuratoin
application = Flask(__name__, template_folder="../templates", static_folder="../static")

'''
Handles GET and POST requests to /.
A get request will be invoked by the browser when browsing to /
A post request will be invoked by the browser when the user submits the form with the email address
'''
@application.route('/', methods=['GET', 'POST'])
def index():
    email = ''
    check_result = ''
    invalid_lines = []

    # check if an email address has been submitted. If so, check the email address vor syntactic correctness
    if request.method == "POST" and "email" in request.form:
        email = request.form["email"]
        check_result = is_email_address_valid(email)
    elif request.method == "POST" and request.files:
        file = request.files['file']
        if file:
            invalid_lines = check_email_addresses(file)

    # render index.html
    return render_template('index.html', email=email, check_result=check_result, invalid_lines=invalid_lines)

@application.route('/api/v1/isEmailAddressValid', methods=['POST']) #respond to POST requests
def api_is_email_address_valid():
    if not request.json or not 'emailAddress' in request.json: #check if request comes with json data containing an email
        return abort(400, "No emailAddress found in request body") #no email in body. abort with error 400 bad request
    print(request.json)
    email = request.json['emailAddress'] #extract email address from json
    response = {"emailAddress": email, "isValid": is_email_address_valid(email)} #create a response dictionary
    return jsonify(response) #return the response as json


@application.route('/api/v1/areEmailAddressesValid', methods=['POST']) #respond to POST requests
def api_are_email_addresses_valid():
    file = request.files.get('file') #extract file from request body
    if not file:        
        return abort(400) #no file found, abrot with status code 400 bad request
    try:            
        return jsonify(check_email_addresses(file)) #check file content and return result as json
    except:
        abort (400, 'Could not parse file {}'.format(file.filename)) #an error happened. return status code 400 bad request
