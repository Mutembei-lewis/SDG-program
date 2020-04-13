from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,SelectField
from wtforms.validators import DataRequired, Length, ValidationError
class  covid19DataForm(FlaskForm):
    name = StringField('Enter the region:', validators =[DataRequired()])
    
    AvgAge = IntegerField('Average population age:' , validators =[DataRequired()])
    AvgDailyIncomeInUSD = IntegerField('Average daily income in US $:' , validators =[DataRequired()])
    AvgDailyIncomePopulation = IntegerField('Average daily income population', validators=[DataRequired()])
    periodType = SelectField('periodType :',choices=[('1', 'days'),('2', 'weeks'),('3','months')])
    timeToElapse = IntegerField('TimeToElapse:')
    reportedCases =IntegerField('reportedCases:', validators =[DataRequired()])
    population = IntegerField('population:', validators =[DataRequired()])
    totalHospitalBeds =IntegerField('total hospital beds:', validators = [DataRequired()])
    submit = SubmitField('submit')