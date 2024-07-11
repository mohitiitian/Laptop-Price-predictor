import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField, SubmitField, IntegerField,FloatField
from wtforms.validators import DataRequired, Optional

# TypeName	Ram	Weight		Touchscreen	IPS Panel	ppi	Brand	HDD	SSD	gpu brand	op s


data = pd.read_csv('updated_data.csv')
data = data.drop(columns = "Price")
class Inputform(FlaskForm):
    Company = SelectField(
        label = "Company",
        choices = data.Company.unique().tolist(),
        validators=[DataRequired()]
    )
    TypeName = SelectField(
        label = "TypeName",
        choices = data.TypeName.unique().tolist(),
        validators=[DataRequired()]
    )
    Ram = IntegerField(
        label = "Ram",
        validators=[DataRequired()]
    )
    Weight = FloatField(
        label = "Weight",
        validators=[DataRequired()]
    )
    Touchscreen = BooleanField(
        label = "Touchscreen",
        validators=[Optional()]
    )
    IPS_Panel = BooleanField(
        label = "IPS Panel",
        validators=[Optional()]
    )
    ppi = SelectField(
        label = "Pixcels per inch",
        choices = data.ppi.unique().tolist(),
        validators=[DataRequired()]
    )
    Brand = SelectField(
        label = "Brand",
        choices = data.Brand.unique().tolist(),
        validators=[DataRequired()]
    )
    HDD = SelectField(
        label = "HDD",
        choices = data.HDD.unique().tolist(),
        validators=[DataRequired()]
    )
    SSD = SelectField(
        label = "SSD",
        choices = data.SSD.unique().tolist(),
        validators=[DataRequired()]
    )
    gpu = SelectField(
        label = "gpu brand",
        choices = data['gpu brand'].unique().tolist(),
        validators=[DataRequired()]
    )
    ops = SelectField(
        label = "op s",
        choices = data['op s'].unique().tolist(),
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")


