from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo


class QuestionForm(FlaskForm):
    subject = StringField(
        "제목",
        validators=[DataRequired(), EqualTo("content", message="Passwords must match")],
    )
    content = TextAreaField("내용", validators=[DataRequired()])
