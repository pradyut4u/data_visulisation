import pandas as pd
import plotly.graph_objects as pgo
import csv
df = pd.read_csv("data.csv")
#print(df.groupby("level").mean())
print(df.groupby("student_id").mean())
fig = pgo.Figure(pgo.Bar(
    x=df.groupby("student_id")["attempt"].mean(),
    y=['TRL_123','TRL_987','TRL_abc','TRL_imb','TRL_mda','TRL_mno','TRL_rst','TRL_xsl','TRL_xyz','TRL_zet','TRL_zny'],
    orientation='h'
))
fig.show()