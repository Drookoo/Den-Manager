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

print("Before length" + str(len(Nulines)))

loop2 = 0
number = 0
s1 = []
s2 = []

while loop2 <=13:
    sumof30 = sum(Nulines[0:29])
    sumof30 = (sumof30) / 30
    s1.append(sumof30)

    loop = 0

    while loop <=29:
        Nulines.pop(0)
        loop = loop + 1

    loop2 = loop2 + 1

while number <= len(s1):
    number = number + 1
    s2.append(number)

print("After length" + str(len(Nulines)))
print(s1)

trace = go.Bar(
    x = ['1:30', '2:00','2:30','3:00', '3:30', '4:00', '4:30', '5:00', '5:30', '6:00', '6:30', '7:00', '7:30', '8:00'],
    y = s1,

)
data = [trace]

plot_url = py.plot(data, filename='basic-line')