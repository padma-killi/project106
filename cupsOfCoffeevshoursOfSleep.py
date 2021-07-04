import csv
import plotly_express as px
import numpy as np

def plottingGraph(dataPath) :
    with open (dataPath) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x = 'Coffee in ml',y = 'sleep in hours',title = 'Corelation of Cups of coffee and Hours of sleep' )
        fig.show()

def getDataSource(dataPath):
    cupsOfCoffee = []
    hoursOfSleep = []
    with open(dataPath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            cupsOfCoffee.append(float(row['Coffee in ml']))
            hoursOfSleep.append(float(row['sleep in hours']))

    return {'x':cupsOfCoffee,'y':hoursOfSleep}


def findCorrelation(datasource):
        correlation = np.corrcoef(datasource["x"],datasource["y"])
        print("Corelation of Cups of coffee and Hours of sleep :- /n -->",correlation[0,1])



def main():
    dataPath = "coffeevshoursOfSleep.csv"
    datasource = getDataSource(dataPath)
    findCorrelation(datasource)
    plottingGraph(dataPath)

main()