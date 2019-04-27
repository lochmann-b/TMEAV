from flask import Flask, render_template, request
from check_email_address_function import check_email_address

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    email = ''
    check_result = ''

    if request.method == "POST" and "email" in request.form:
        email = request.form["email"]
        check_result = check_email_address(email)

    return render_template('index.html', email=email, check_result=check_result)
