import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.graph_objs as go
import plotly.plotly as py

plotly.tools.set_credentials_file(
            username='nachozombie',
            api_key='ajvmmn1scx'
        )

text_file = open("data.txt", "r")
lines = text_file.read().split(':')
newlines = [s for s in lines if len(s) > 3]
newnewlines = [s for s in newlines if len(s) < 16]

Nulines = ([s.strip(' \nTimeStamp ') for s in newnewlines])
Nulines.pop(0)
print(Nulines)

text_file.close()
Nulines = list(map(int,Nulines))

s1 = [];
number = 0

while number <= len(Nulines):
    number = number + 1
    s1.append(number)


trace = go.Scatter(
    x = s1,
    y = Nulines,
    mode = 'markers'
)
data = [trace]



plot_url = py.plot(data, filename='basic-line')