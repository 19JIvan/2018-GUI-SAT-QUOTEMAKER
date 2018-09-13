from tkinter import *
import csv
from tables import createStandardTable as cst

class QTEGUI:

    def __init__(self, master):

        def pastQuotesB():

            self.Spacer3.grid_remove()
            self.pageTitle1.grid_remove()
            self.priceSettings.grid_remove()
            self.cakeFlavour.grid_remove()
            self.cakeFlavourE.grid_remove()
            self.cakeType.grid_remove()
            self.cakeTypeE.grid_remove()
            self.numberOfPeople.grid_remove()
            self.numberOfPeopleE.grid_remove()
            self.numberOfTiers.grid_remove()
            self.numberOfTiersE.grid_remove()
            self.decorations.grid_remove()
            self.decorationsE.grid_remove()
            self.icing.grid_remove()
            self.icingE.grid_remove()
            self.extras.grid_remove()
            self.extrasE.grid_remove()
            self.dateRequired.grid_remove()
            self.dateRequiredE.grid_remove()
            self.total.grid_remove()
            self.totalD.grid_remove()
            self.calulateB.grid_remove()
            #self.photoI.grid_remove()
            self.printB.grid_remove()
            pastQuotes()

        def pastQuotes():

            self.Spacer3.grid()
            self.pageTitle2.grid()
            self.searchPQ.grid()
            tableFrame.grid()

        def newQuoteB():

            self.Spacer3.grid_remove()
            self.pageTitle2.grid_remove()
            self.searchPQ.grid_remove()
            tableFrame.grid_remove()
            #self.pageTitle1.grid_remove()
            #self.priceSettings.grid_remove()
            #self.cakeFlavour.grid_remove()
            #self.cakeFlavourE.grid_remove()
            #self.cakeType.grid_remove()
            #self.cakeTypeE.grid_remove()
            #self.numberOfPeople.grid_remove()
            #self.numberOfPeopleE.grid_remove()
            #self.numberOfTiers.grid_remove()
            #self.numberOfTiersE.grid_remove()
            #self.decorations.grid_remove()
            #self.decorationsE.grid_remove()
            #self.icing.grid_remove()
            #self.icingE.grid_remove()
            #self.extras.grid_remove()
            #self.extrasE.grid_remove()
            #self.dateRequired.grid_remove()
            #self.dateRequiredE.grid_remove()
            #self.total.grid_remove()
            #self.totalD.grid_remove()
            #self.calulateB.grid_remove()
            # self.photoI.grid_remove()
            #self.printB.grid_remove()
            newQuote()

        def newQuote():
            self.Spacer3.grid()
            self.pageTitle1.grid()
            self.priceSettings.grid()
            self.cakeFlavour.grid()
            self.cakeFlavourE.grid()
            self.cakeType.grid()
            self.cakeTypeE.grid()
            self.numberOfPeople.grid()
            self.numberOfPeopleE.grid()
            self.numberOfTiers.grid()
            self.numberOfTiersE.grid()
            self.decorations.grid()
            self.decorationsE.grid()
            self.icing.grid()
            self.icingE.grid()
            self.extras.grid()
            self.extrasE.grid()
            self.dateRequired.grid()
            self.dateRequiredE.grid()
            self.total.grid()
            self.totalD.grid()
            self.calulateB.grid()
            #self.photoI.grid()
            self.printB.grid()


        def startUpB():

            self.spacer9 = Label(Frame3, text="1                                                  1")
            self.spacer9.grid(row=1, column=2, columnspan=2, sticky=N)

            self.pageTitle2 = Label(Frame3, text="PAST QUOTES")
            self.pageTitle2.config(font=("TkDefaultFont", 30))
            self.pageTitle2.grid(row=2, column=2, columnspan=2, sticky=N)

            self.searchPQ = Label(Frame3, text="Search: ")
            self.searchPQ.grid(row=3, column=1, sticky=NW)

            table1()
            tableFrame.grid(row=8, column=1, columnspan=5, sticky=N)

            self.pageTitle2.grid_remove()
            self.searchPQ.grid_remove()
            tableFrame.grid_remove()

            #startUpC()

        def startUpA():

            self.Spacer3 = Label(Frame3, text="1                                                                                                             1", height=0)
            self.Spacer3.config(bg="White", foreground="White")
            self.Spacer3.grid(row=1, column=1, sticky=W, columnspan=5)

            self.pageTitle1 = Label(Frame3, text="NEW QUOTE")
            self.pageTitle1.config(font=("TkDefaultFont", 30))
            self.pageTitle1.grid(row=2, column=2, columnspan=2, sticky=N)

            self.priceSettings = Button(Frame3, width=10, height=1, text="Price Settings")
            self.priceSettings.grid(row=2, column=1, sticky=NW)

            self.cakeFlavour = Label(Frame3, text="Cake Flavour:")
            self.cakeFlavour.grid(row=3, column=2, sticky=W)

            self.cakeFlavourE = Entry(Frame3, width=15)
            self.cakeFlavourE.grid(row=3, column=3, sticky=W)

            self.cakeType = Label(Frame3, text="Cake Type:")
            self.cakeType.grid(row=4, column=2, sticky=W)

            self.cakeTypeE = Entry(Frame3, width=15)
            self.cakeTypeE.grid(row=4, column=3, sticky=W)

            self.numberOfPeople = Label(Frame3, text="Number Of People:")
            self.numberOfPeople.grid(row=5, column=2, sticky=W)

            self.numberOfPeopleE = Entry(Frame3, width=15)
            self.numberOfPeopleE.grid(row=5, column=3, sticky=W)

            self.numberOfTiers = Label(Frame3, text="Number Of Tiers:")
            self.numberOfTiers.grid(row=6, column=2, sticky=W)

            self.numberOfTiersE = Entry(Frame3, width=15)
            self.numberOfTiersE.grid(row=6, column=3, sticky=W)

            self.decorations = Label(Frame3, text="Decorations:")
            self.decorations.grid(row=7, column=2, sticky=W)

            self.decorationsE = Entry(Frame3, width=15)
            self.decorationsE.grid(row=7, column=3, sticky=W)

            self.icing = Label(Frame3, text="Icing:")
            self.icing.grid(row=8, column=2, sticky=W)

            self.icingE = Entry(Frame3, width=15)
            self.icingE.grid(row=8, column=3, sticky=W)

            self.extras = Label(Frame3, text="Extras:")
            self.extras.grid(row=9, column=2, sticky=W)

            self.extrasE = Entry(Frame3, width=15)
            self.extrasE.grid(row=9, column=3, sticky=W)

            self.dateRequired = Label(Frame3, text="Date Required:")
            self.dateRequired.grid(row=10, column=2, sticky=W)

            self.dateRequiredE = Entry(Frame3, width=15)
            self.dateRequiredE.grid(row=10, column=3, sticky=W)

            self.total = Label(Frame3, text="total:")
            self.total.grid(row=11, column=2, sticky=W)

            self.totalD = Label(Frame3, text="Variable")
            self.totalD.grid(row=11, column=3, sticky=W)

            self.calulateB = Button(Frame3, text="Calulate")
            self.calulateB.grid(row=12, column=4, sticky=E)

            #self.photoI = Image(Frame3)
            #self.photoI.grid(row=13, column=1, rowspan=5, columnspan=5, sticky=N)

            self.printB = Button(Frame3, text="Print")
            self.printB.grid(row=18, column=4, sticky=E)

            self.Spacer3.grid_remove()
            self.pageTitle1.grid_remove()
            self.priceSettings.grid_remove()
            self.cakeFlavour.grid_remove()
            self.cakeFlavourE.grid_remove()
            self.cakeType.grid_remove()
            self.cakeTypeE.grid_remove()
            self.numberOfPeople.grid_remove()
            self.numberOfPeopleE.grid_remove()
            self.numberOfTiers.grid_remove()
            self.numberOfTiersE.grid_remove()
            self.decorations.grid_remove()
            self.decorationsE.grid_remove()
            self.icing.grid_remove()
            self.icingE.grid_remove()
            self.extras.grid_remove()
            self.extrasE.grid_remove()
            self.dateRequired.grid_remove()
            self.dateRequiredE.grid_remove()
            self.total.grid_remove()
            self.totalD.grid_remove()
            self.calulateB.grid_remove()
            #self.photoI.grid_remove()
            self.printB.grid_remove()

            startUpB()

        self.master = master,
        master.title("Quote Maker")

        Frame1 = Frame(root, width=100, highlightbackground="#51504D", highlightcolor="#51504D", highlightthickness=7)
        Frame2 = Frame(Frame1, width=42, bg="#A19C95")
        Frame3 = Frame(Frame2, width=40, bg="white")

        #for i in range(0,11):
        #    self.p = Label(master, text=i)
        #    self.o = Label(master, text=i)
        #    self.p.grid(row=i, column=0)
        #    self.o.grid(row=0, column=i)

        #for i in range(0,11):
        #    self.p = Label(Frame1, text=i)
        #    self.o = Label(Frame1, text=i)
        #    self.p.grid(row=i, column=0)
        #    self.o.grid(row=0, column=i)

        #for i in range(0,11):
        #    self.p = Label(Frame2, text=i)
        #    self.o = Label(Frame2, text=i)
        #    self.p.grid(row=i, column=0)
        #    self.o.grid(row=0, column=i)

        #for i in range(0,11):
        #   self.p = Label(Frame3, text=i)
        #   self.o = Label(Frame3, text=i)
        #   self.p.grid(row=i, column=0)
        #   self.o.grid(row=0, column=i)

        tableFrame = Frame(Frame3)

        def table1():
            # Your csv file can contain as many rows and colums as needed
            f = open("films.csv")

            # note here I have sent it root but you can also send it a frame
            self.newtable = cst(f, tableFrame)
            self.newtable.grid()

        self.titleText = Label(master, text="Bella Cake Art", height=1)
        self.titleText.grid(row=1, column=1, sticky=W),

        self.settingsButton = Button(master, text="Settings", height=1)
        self.settingsButton.grid(row=1, column=5, sticky=E)

        self.Spacer = Label(Frame2, text="1                                                                                                             1", height=1)
        self.Spacer.config(bg="#A19C95", foreground="#A19C95")
        self.Spacer.grid(row=2, column=1, sticky=W, columnspan=5)

        self.menuBarNQ = Button(Frame2, text="New Quote", width=10, highlightbackground="#A19C95", height=1, command=newQuoteB)
        self.menuBarNQ.config(font=("TkDefaultFont", 18))
        self.menuBarNQ.grid(row=2, column=2, sticky=NW)

        self.menuBarPQ = Button(Frame2, text="Past Quotes", width=10, highlightbackground="#A19C95", height=1,
                                command=pastQuotesB)
        self.menuBarPQ.config(font=("TkDefaultFont", 18))
        self.menuBarPQ.grid(row=2, column=3, sticky=N)

        self.menuBarMP = Button(Frame2, text="Monthly Profit", width=10, highlightbackground="#A19C95", height=1)
        self.menuBarMP.config(font=("TkDefaultFont", 18))
        self.menuBarMP.grid(row=2, column=4, sticky=NE)

        run = startUpA()
        run

        Frame1.grid(row=2, column=1, columnspan=5)
        Frame2.grid(row=1, column=1, columnspan=5)
        Frame3.grid(row=3, column=1, columnspan=5)

root = Tk()
root.geometry("390x800")
#root.resizable(width=False, height=False)
gui = QTEGUI(root)
root.mainloop()