import os
from flask import Flask, render_template, request, send_from_directory, jsonify, abort
from app.email_utils import are_email_addresses_valid, is_email_address_valid

from app.customers_xml_parser import check_email_addresses, split_email_addresses

# configuratoin
application = Flask(__name__, template_folder="../templates",
                    static_folder="../static")

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
        check_result = are_email_addresses_valid(email)
    elif request.method == "POST" and request.files:
        file = request.files['file']
        if file:
            invalid_lines = check_email_addresses(file)

    # render index.html
    return render_template('index.html', email=email, check_result=check_result, invalid_lines=invalid_lines)


@application.route('/splitter', methods=['GET', 'POST'])
def xml_file_splitter():
    lines = []
    if request.method == "POST" and request.files:
        file = request.files['file']
        chunkSize = int(request.form['chunkSize'])

        if file:
            lines = split_email_addresses(file, chunkSize)            

    # render index.html
    return render_template('splitter.html',  lines=lines)


###########
# WEB API #
###########

# respond to POST requests
@application.route('/api/v1/isEmailAddressValid', methods=['POST'])
def api_is_email_address_valid():
    # check if request comes with json data containing an email
    if not request.json or not 'emailAddress' in request.json:
        # no email in body. abort with error 400 bad request
        return abort(400, "No emailAddress found in request body")
    print(request.json)
    email = request.json['emailAddress']  # extract email address from json
    # create a response dictionary
    response = {"emailAddress": email,
                "isValid": is_email_address_valid(email)}
    return jsonify(response)  # return the response as json


# respond to POST requests
@application.route('/api/v1/areEmailAddressesValid', methods=['POST'])
def api_are_email_addresses_valid():
    file = request.files.get('file')  # extract file from request body
    if not file:
        # no file found, abrot with status code 400 bad request
        return abort(400)
    try:
        # check file content and return result as json
        return jsonify(check_email_addresses(file))
    except:
        # an error happened. return status code 400 bad request
        abort(400, 'Could not parse file {}'.format(file.filename))
