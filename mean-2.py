#mean
import plotly
import plotly.graph_objs as go
import plotly.plotly as py

plotly.tools.set_credentials_file(
            username='SirAngelOfYork',
            api_key='wSDumMEWX7nHxL6C41UT'
        )
text_file = open("13hrs", "r")
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

while loop2 <=14:
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
    x = ['Midnight', '12:30am','1:00am','1:30am', '2:00am', '2:30am', '3:00am', '3:30am', '4:00am', '4:30am', '5:00am', '5:30am', '6:30am', '7:00am', '7:30am'],
    y = s1,

)
data = [trace]

plot_url = py.plot(data, filename='basic-line')