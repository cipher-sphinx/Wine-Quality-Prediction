from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class PredictionForm(FlaskForm):
    fixed_acidity = StringField('Fixed Acidity', validators=[validators.InputRequired()])
    volatile_acidity = StringField('Volatile Acidity', validators=[validators.InputRequired()])
    citric_acid = StringField('Citric Acid', validators=[validators.InputRequired()])
    residual_sugar = StringField('Residual Sugar', validators=[validators.InputRequired()])
    chlorides = StringField('Chlorides', validators=[validators.InputRequired()])
    free_sulfur_dioxide = StringField('Free Sulfur Dioxide', validators=[validators.InputRequired()])
    total_sulfur_dioxide = StringField('Total Sulfur Dioxide', validators=[validators.InputRequired()])
    density = StringField('Density', validators=[validators.InputRequired()])
    pH = StringField('pH', validators=[validators.InputRequired()])
    sulphates = StringField('Sulphates', validators=[validators.InputRequired()])
    alcohol = StringField('Alcohol', validators=[validators.InputRequired()])
    submit = SubmitField('Predict')
