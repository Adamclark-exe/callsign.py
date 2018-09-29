import random
from tkinter import *

class CallsignGenerator () :
    origFirst = ""
    origLast = ""

    firstList= ["Agile","Able","Proud","Just","Electric","Nimble","Swift","Silent","Saucy","Bold","Bold","Viscious","Icy"]
    lastList = ["Cobra","Badger","Bones","Dagger",]

    #methods
    def __init__(self,firstDate, lastDate):
        self.origFirst = firstDate
        self.origLast = lastDate

    def CreateName (self) :
        x= random.randint(0, len (self.firstList) -1)
        y=random.randint(0, len (self.lastList) -1)
        return self.firstList [x] + self.lastList [y]


def buttonClick():
    #get the info out of the boxes
    first = fText.get()
    last = lText.get()
    
    #Create an instance of our generator class
    mygen = CallsignGenerator(first, last)
    
    #run the generator
    cSign = mygen.CreateName()
                                    
    #show it on the screen
    output.config (text = cSign, image=Banner, compound = CENTER)

                
root = Tk()

Banner = PhotoImage(file="USAF_Symbol.gif")
Banner = Banner.subsample(4,4)

ft = "verdana 14"
title = Label (root, text= "what's your Aviator Callsign?", font="Verdana 20")
fLabel = Label(root, text="Month", font= ft)
fText = Entry(root, font="Verdana 14")
lLabel = Label(root, text="Day", font= ft)
lText = Entry(root, font="Verdana 14")
btn = Button(root, font = ft, text="generate name", command=buttonClick)
output = Label(root, image=Banner)

title.pack()
fLabel.pack()
fText.pack()
lLabel.pack()
lText.pack()
btn.pack()
output.pack()

root.mainloop()
