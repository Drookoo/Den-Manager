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

    if current > (Max * newPC):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("andrewku123@gmail.com", "nach0zombie")

        msg = "Your venue is at " + oldPC + "% capacity"
        server.sendmail("andrewku123@gmail.com", "andrewku123@gmail.com", msg)
        server.quit()


    with open("newhrs", "a") as myfile:
        myfile.write("TimeStamp: " + str(datetime.now().time())+"\t" + "Person Count:" + str(current) + "\n")

    time.sleep(60)