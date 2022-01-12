import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    temperature=[]
    icecream_sales=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            temperature.append(float(row["Coffee in ml"]))
            icecream_sales.append(float(row["sleep in hours"]))
    return{"x":temperature,"y":icecream_sales}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Coffee in ml and sleep in hours is : ",correlation[0,1])

def setup():
    data_path="coffe-sleep.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()