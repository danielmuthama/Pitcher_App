from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms import validators
from wtforms.fields.core import RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title', validators=[Required()])
    name = TextAreaField('Pitch', validators=[Required()])
    author = StringField('Author : ', validators=[Required()])
    category = RadioField('Pitch Category', choices=[('pickup_lines', 'pickup_lines'), ('interview_pitch', 'interview_pitch'), ('product_pitch', 'product_pitch'), ('promotion_pitch', 'promotion_pitch')])
    submit = SubmitField('Submit')