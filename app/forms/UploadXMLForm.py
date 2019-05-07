from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired



class UploadXMLForm(FlaskForm):
    file = FileField("Upload an XML File", validators=[FileRequired(), FileAllowed(['xml'], 'XML Files Only')])
    submit = SubmitField("Validate")
