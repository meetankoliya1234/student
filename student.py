import pandas as pd
from pandas.core import groupby
import plotly.express as px

df = pd.read_csv('./data.csv')
print(df.groupby("level")['attempt'].mean())

fig = px.scatter(df, x = "student_id", y = "attempt", color = "level")

fig.show()