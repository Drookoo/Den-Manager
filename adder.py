import plotly
import plotly.graph_objs as go
import plotly.plotly as py

plotly.tools.set_credentials_file(
            username='SirAngelOfYork',
            api_key='wSDumMEWX7nHxL6C41UT'
        )

text_file = open("newhrs", "r")
lines = text_file.read().split(':')
newlines = [s for s in lines if len(s) > 3]
newnewlines = [s for s in newlines if len(s) < 16]

Nulines = ([s.strip(' \nTimeStamp ') for s in newnewlines])
Nulines.pop(0)

text_file.close()
Nulines = list(map(int,Nulines))

print("Before length " + str(len(Nulines)))

Nulines = [x + 94 for x in Nulines]

print(Nulines)

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

point = input("Point 1 = ")
print(Nulines[int(point) - 1])
point2 = input("Point 2 = ")
print(Nulines [int(point2) - 1])
x1 = int(point) - 1
x2 = int(point2) - 1
y1 = Nulines[int(point) - 1]
y2 = Nulines [int(point2) - 1]

print("Slope between these two points in " + str(x2 - x1) + " Minutes is: ")
print( str(y2 - y1))