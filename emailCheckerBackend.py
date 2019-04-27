from flask import Flask, render_template, request
from check_email_address_function import check_email_address

app = Flask(__name__)


'''
Handles GET and POST requests to /.
A get request will be invoked by the browser when browsing to /
A post request will be invoked by the browser when the user submits the form with the email address
'''
@app.route('/', methods=['GET', 'POST']) 
def index():
    email = ''
    check_result = ''

    #check if an email address has been submitted. If so, check the email address vor syntactic correctness
    if request.method == "POST" and "email" in request.form:
        email = request.form["email"]
        check_result = check_email_address(email)

    #render index.html
    return render_template('index.html', email=email, check_result=check_result)