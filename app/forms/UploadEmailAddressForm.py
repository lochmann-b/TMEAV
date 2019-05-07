from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UploadEmailAddressForm(FlaskForm):
    email = StringField("Enter one or more email adresses separated by a ; sign", validators=[DataRequired()])
    submit = SubmitField("Validate")
