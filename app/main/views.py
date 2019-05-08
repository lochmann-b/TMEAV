from flask import render_template, session, url_for
from . import main
from .. import db
from ..models import User
from .forms import UploadEmailAddressForm
from .forms import UploadXMLForm
from .forms import SplitXMLForm
from .email_utils import are_email_addresses_valid, is_email_address_valid
from .customers_xml_parser import check_email_addresses, split_email_addresses

'''
Handles GET and POST requests to /.
A get request will be invoked by the browser when browsing to /
A post request will be invoked by the browser when the user submits the form with the email address
'''
@main.route('/', methods=['GET', 'POST'])
def index():
    email = ''
    check_result = ''
    invalid_lines = []

    #create form
    form = UploadEmailAddressForm()

    if form.validate_on_submit():
        email = form.email.data
        check_result = are_email_addresses_valid(email)
        form.email.data=''
    
    return render_template('index.html', formUploadEmail=form, email=email, check_result=check_result)


@main.route('/xmlupload', methods=['GET', 'POST'])
def uploadxml():
    email = ''
    check_result = ''
    invalid_lines = []

    form = UploadXMLForm()

    # check if an email address has been submitted. If so, check the email address vor syntactic correctness
    if form.validate_on_submit():      
        file = form.file.data
        invalid_lines = check_email_addresses(file)

    # render index.html
    return render_template('xmlupload.html', form=form, invalid_lines=invalid_lines)


@main.route('/splitter', methods=['GET', 'POST'])
def xml_file_splitter():
    lines = []
    form = SplitXMLForm()  
    if form.validate_on_submit():
        file = form.file.data
        chunk_size = int(form.chunk_size.data)
        lines = split_email_addresses(file, chunk_size)            

    # render index.html
    return render_template('splitter.html', form=form, lines=lines)


###########
# WEB API #
###########

# respond to POST requests
@main.route('/api/v1/isEmailAddressValid', methods=['POST'])
def api_is_email_address_valid():
    # check if request comes with json data containing an email
    if not request.json or not 'emailAddress' in request.json:
        # no email in body. abort with error 400 bad request
        return abort(400, "No emailAddress found in request body")
    email = request.json['emailAddress']  # extract email address from json
    # create a response dictionary
    response = {"emailAddress": email,
                "isValid": is_email_address_valid(email)}
    return jsonify(response)  # return the response as json


# respond to POST requests
@main.route('/api/v1/areEmailAddressesValid', methods=['POST'])
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
