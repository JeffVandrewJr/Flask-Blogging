from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField,\
        SelectField
from wtforms.validators import DataRequired


class BlogEditor(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    text = TextAreaField("text", validators=[DataRequired()])
    tags = SelectField(
        'Optional Parameters',
        choices=[
            ('noemail', 'Do Not Email this Update'),
            ('public', 'Post this to homepage rather than updates.')
        ]
    )
    draft = BooleanField("draft", default=False)
    submit = SubmitField("submit")
