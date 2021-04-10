import pandas as pd
import plotly.graph_objects as pgo
import csv
df=pd.read_csv("data.csv")
print(df.groupby("level").mean())
fig=pgo.Figure(pgo.Bar(
    x=df.groupby("level").mean()["attempt"],
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'
))
fig.show()