import os
from flask import Flask, request, render_template,redirect,url_for
from forms import covid19DataForm
import math

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mykey'
@app.route('/',methods=['GET','POST'])
def index():
    form = covid19DataForm()
    return render_template('index.html', form = form)

@app.route('/covid19ImpactEstimator',methods=['GET','POST'])
def  covid19ImpactEstimator():
    form = covid19DataForm()
   
    class covidImpactEstimator():
        form = covid19DataForm()
        covid19DataInput =  {
                'region': { 'name':form.name.data,'AvgAge':form.AvgAge.data,'AvgDailyIncomeInUSD':form.AvgDailyIncomeInUSD.data,'AvgDailyIncomePopulation': form.AvgDailyIncomePopulation.data},
                'periodType':form.periodType.data,
                'timeToElapse':form.timeToElapse.data,
                'reportedCases':form.reportedCases.data,
                'population': form.population.data,
                'totalHospitalBeds': form.totalHospitalBeds.data
                }
        name = covid19DataInput['region']['name']
        AvgAge = covid19DataInput['region']['AvgAge']
        AvgDailyIncomeInUSD = covid19DataInput['region']['AvgDailyIncomeInUSD']
        AvgDailyIncomePopulation = covid19DataInput['region']['AvgDailyIncomePopulation']
        periodType = covid19DataInput['periodType']
        timeToElapse = covid19DataInput['timeToElapse']
        reportedCases =covid19DataInput['reportedCases']
        population = covid19DataInput['population']
        totalHospitalBeds =covid19DataInput['totalHospitalBeds']
        name =name
        reportedCases=reportedCases
        population=population
        totalHospitalBeds = totalHospitalBeds
        timeToElapse=timeToElapse
        AvgDailyIncomeInUSD = AvgDailyIncomeInUSD
        AvgDailyIncomePopulation =AvgDailyIncomePopulation




        if periodType == '1':
                timeToElapse = timeToElapse

        elif periodType == '2':
                timeToElapse *=7

        elif periodType == '3':
                timeToElapse *= 30

            
    class ImpactForm(covidImpactEstimator):
            impact = covidImpactEstimator()   
            currentlyInfected =impact.reportedCases*10
            factor= math.floor(impact.timeToElapse/3)
                    
            InfectionByRequestedTime = currentlyInfected * 2^factor
            severeCasesByRequestedTime = 15% InfectionByRequestedTime
            available_beds = 35% (95%impact.totalHospitalBeds)
            hospitalBedsByRequestedTime= severeCasesByRequestedTime -available_beds
            casesForICUByRequestedTime = 5% InfectionByRequestedTime
            casesForVentilatorsByRequestedTime = 2% InfectionByRequestedTime
            populationPercentageEarningAverageIncome =impact.AvgDailyIncomePopulation/impact.population
            dollarsInFlight = InfectionByRequestedTime * (populationPercentageEarningAverageIncome/100) * impact.AvgDailyIncomeInUSD * impact.timeToElapse

                # def severeImpact():
    class SevereImpact(covidImpactEstimator):
            impact = covidImpactEstimator()

            currentlyInfected = impact.reportedCases * 50
            factor= math.floor(impact.timeToElapse/3)
            InfectionByRequestedTime = currentlyInfected * 2^factor
            severeCasesByRequestedTime = 15% InfectionByRequestedTime
            available_beds = 35% (95%impact.totalHospitalBeds)
            hospitalBedsByRequestedTime = severeCasesByRequestedTime -available_beds
            casesForICUByRequestedTime = 5% InfectionByRequestedTime
            casesForVentilatorsByRequestedTime = 2% InfectionByRequestedTime
            populationPercentageEarningAverageIncome =impact.AvgDailyIncomePopulation/impact.population
            dollarsInFlight = InfectionByRequestedTime * (populationPercentageEarningAverageIncome/100) *impact.AvgDailyIncomeInUSD *impact.timeToElapse
        # class OutputData(covidImpactEstimator):
    estimate = covidImpactEstimator()
    impact = ImpactForm()
    severeImpact = SevereImpact()
          
    result_dict = {
                'region': {'name': estimate.name,'AvgAge':estimate.AvgAge,'AvgDailyIncomeInUSD':estimate.AvgDailyIncomeInUSD,'AvgDailyIncomePopulation': estimate.AvgDailyIncomePopulation},
                'population':estimate.population,
                'reportedCases':estimate.reportedCases,
                'periodType': estimate.periodType,
                'timeToElapse':estimate.timeToElapse,
                'totalHospitalBeds':estimate.totalHospitalBeds,
                
                }
            
    impact_data ={
                    'currentlyInfected': impact.currentlyInfected,
                    'InfectionByRequestedTime':impact.InfectionByRequestedTime,
                    'severeCasesByRequestedTime':impact.severeCasesByRequestedTime,
                    'available_beds': impact.available_beds,
                    'hospitalBedsByRequestedTime': impact.hospitalBedsByRequestedTime,
                    'casesForIcuByRequestedTime': impact.casesForICUByRequestedTime,
                    'casesForVentilatorsByRequestedTime':impact.casesForVentilatorsByRequestedTime,
                    'dollarsInFlight': impact.dollarsInFlight

             }
    severeImpact ={
                    'currentlyInfected':severeImpact.currentlyInfected,
                    'InfectionByRequestedTime':severeImpact.InfectionByRequestedTime,
                    'severeCasesByRequestedTime':severeImpact.severeCasesByRequestedTime,
                    'available_beds': severeImpact.available_beds,
                    'hospitalBedsByRequestedTime': severeImpact.hospitalBedsByRequestedTime,
                    'casesForIcuByRequestedTime': severeImpact.casesForICUByRequestedTime,
                    'casesForVentilatorsByRequestedTime':severeImpact.casesForVentilatorsByRequestedTime,
                    'dollarsInFlight': severeImpact.dollarsInFlight
            }
        # outputdata =OutputData()
    return render_template('results.html',data =result_dict,impact =impact_data ,severeImpact =severeImpact)

if __name__ == "__main__":
    app.run(debug = True)