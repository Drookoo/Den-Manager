from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import plotly
from plotly.graph_objs import *
import plotly.plotly as py

#Overcrowd          Max is 675
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

    # GUI
    top = Tk()
    top.geometry("300x300")
    def helloCallBack():
        msg = messagebox.showinfo("Current Number of People", "There are currently " + str(current) + " people aat HackNYU")
    B = Button(top, text="Current Number of People", command=helloCallBack)
    B.place(x=50, y=50)


    if Max > 1:
        top.mainloop()

        plotly.tools.set_credentials_file(
            username='nachozombie',
            api_key='ajvmmn1scx'
        )
        gaussian_numbers = np.random.randn(1000)
        plt.hist(gaussian_numbers)
        plt.title("Gaussian Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")

        fig = plt.gcf()

        plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')
    with open("data.txt", "a") as myfile:
        myfile.write("TimeStamp: " + str(datetime.now().time())+"\t" + "Person Count:" + str(current) + "\n")

    time.sleep(60)

