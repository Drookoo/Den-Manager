from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime
import smtplib
#Overcrowd          Max is 675

#Max = 675
#oldPC = input("%?")
#newPC = int(oldPC) * .01

#logging
while True:

    Max = 675
    oldPC = input("%?")
    newPC = int(oldPC) * .01

    url = "http://livecount.hacknyu.org/"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    current = int("".join(soup.find("div", {"id": "currentcount"}).strings))

    with open("newhrs", "a") as myfile:
        myfile.write("TimeStamp: " + str(datetime.now().time())+"\t" + "Person Count:" + str(current) + "\n")

    if current > (Max * newPC):

        text_file = open("newhrs", "r")
        lines = text_file.read().split(':')
        newlines = [s for s in lines if len(s) > 3]
        newnewlines = [s for s in newlines if len(s) < 16]

        Nulines = ([s.strip(' \nTimeStamp ') for s in newnewlines])
        Nulines.pop(0)

        Nulines = list(map(int, Nulines))
        Nulines = [x + 94 for x in Nulines]
        s1 = [];
        number = 0

        while number <= len(Nulines):
            number = number + 1
            s1.append(number)
        new1 = (Nulines[len(Nulines) - 1])
        new2 = (Nulines[len(Nulines)- 6])

        x1 = int(new1) - 1
        x2 = int(new2) - 1
        y1 = Nulines[int(new1) - 1]
        y2 = Nulines[int(new2) - 1]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("andrewku123@gmail.com", "nach0zombie")

        msg = "Your venue is at " + oldPC + "% capacity. Your venue will close in "+ str(y2 - y1) + " Minutes"
        server.sendmail("andrewku123@gmail.com", "andrewku123@gmail.com", msg)
        server.quit()

    time.sleep(60)