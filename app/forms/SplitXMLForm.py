from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired



class SplitXMLForm(FlaskForm):
    file = FileField("Split a XML File", validators=[FileRequired(), FileAllowed(['xml'], 'XML Files Only')])
    choices = list(map(lambda x: (str(x), str(x)), range(50, 1000, 50)))
    chunk_size = SelectField(u'Chunk size', choices=choices, default='500')
    submit = SubmitField("Split")
