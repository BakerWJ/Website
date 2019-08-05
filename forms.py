from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    zip = IntegerField('ZIP Code', validators=[DataRequired()])
    sqft = IntegerField('Square Footage', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    beds = FloatField("Beds", validators=[DataRequired()])
    baths = FloatField("Baths", validators=[DataRequired()])
    levels = StringField("Levels", validators=[DataRequired()])
    lotsize = IntegerField("lotsize", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    remarks = StringField("Other comments")
    proptype = SelectField("Property Type", choices=[('SF', 'Single Family'), ('MF', 'Multifamily'), ("CC", 'Condo')])
    button = SubmitField('Search')
