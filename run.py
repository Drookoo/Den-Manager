from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime

#Overcrowd          Max is 675
Binary = 1
Max = 675
oldPC = input("%?")
newPC = int(oldPC) * .01

#if current > (Max * newPC):
#if current < Max:
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.starttls()
    #server.login("andrewku123@gmail.com", "pword")

    #msg = "Your venue is at " + oldPC + "% capacity"
    #server.sendmail("andrewku123@gmail.com", "andrewku123@gmail.com", msg)
    #server.quit()

#logging
while True:
    url = "http://livecount.hacknyu.org/"
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    current = int("".join(soup.find("div", {"id": "currentcount"}).strings))


    with open("13hrs", "a") as myfile:
        myfile.write("TimeStamp: " + str(datetime.now().time())+"\t" + "Person Count:" + str(current) + "\n")
    Binary = 0
    time.sleep(60)

