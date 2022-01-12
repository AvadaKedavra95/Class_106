import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
        fig.show()

def getDataSource(data_path):
    temperature=[]
    icecream_sales=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            temperature.append(float(row["Temperature"]))
            icecream_sales.append(float(row["Ice-cream Sales"]))
    return{"x":temperature,"y":icecream_sales}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Temperature and Ice-Cream sales is : ",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()