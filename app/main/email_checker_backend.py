import os
from flask import Flask, render_template, request, send_from_directory
from app.email_utils import is_email_address_valid
from werkzeug.utils import secure_filename
from app.customers_xml_parser import check_email_addresses

app = Flask(__name__, template_folder="../templates", static_folder="../static")


'''
Handles GET and POST requests to /.
A get request will be invoked by the browser when browsing to /
A post request will be invoked by the browser when the user submits the form with the email address
'''
@app.route('/', methods=['GET', 'POST'])
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
            filename = secure_filename(file.filename)
            invalid_lines = check_email_addresses(file)

    # render index.html
    return render_template('index.html', email=email, check_result=check_result, invalid_lines=invalid_lines)
