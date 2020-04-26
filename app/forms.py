from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed



class UploadForm(FlaskForm):
    description  = TextAreaField('Description',
        validators=[DataRequired(), InputRequired()])

    photo = FileField('Photo', 
        validators=[FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])])

