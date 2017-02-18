import matplotlib.pyplot as plt
import numpy as np
import plotly
from plotly.graph_objs import *
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

#gaussian_numbers = np.random.randn(1000)
#plt.hist(gaussian_numbers)
#plt.title("Gaussian Histogram")
#plt.xlabel("Value")
#plt.ylabel("Frequency")

#fig = plt.gcf()

#plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')