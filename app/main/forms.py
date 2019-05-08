from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class SplitXMLForm(FlaskForm):
    file = FileField("Split a XML File", validators=[FileRequired(), FileAllowed(['xml'], 'XML Files Only')])
    choices = list(map(lambda x: (str(x), str(x)), range(50, 1000, 50)))
    chunk_size = SelectField(u'Chunk size', choices=choices, default='500')
    submit = SubmitField("Split")

class UploadEmailAddressForm(FlaskForm):
    email = StringField("Enter one or more email adresses separated by a ; sign", validators=[DataRequired()])
    submit = SubmitField("Validate")

class UploadXMLForm(FlaskForm):
    file = FileField("Upload an XML File", validators=[FileRequired(), FileAllowed(['xml'], 'XML Files Only')])
    submit = SubmitField("Validate")
