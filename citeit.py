import time
from datetime import datetime
import sys
global authorname
global pagename
global sitename
global createdate

def buildref():
    global authorname
    global pagename
    global sitename
    global createdate
    print("CiteIt - MLA Web Citation Creator - By Meorge")
    print("Type the author's name here (example: \"Jobs, Steve\").")
    authorname = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the page's name here (example: \"Great Places To Visit in Hawaii\").")
    pagename = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the site's name here (example: \"BestTop10\").")
    sitename = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the date it was created if there was one. If there wasn't one, type \"none\".")
    createdate = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    createcitation()

def createcitation():
    global authorname
    global pagename
    global sitename
    global createdate
    print("Now working on your citation...")
    time.sleep(4)
    x = datetime.now()
    currentmonth = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[max(min(int(x.month) - 1, 12), 1)]
    nowtime = str(x.day) + " " + currentmonth + ". " + str(x.year)
    # nowtime = datetime.day() + " " + datetime.month() + " " + datetime.year()
    if createdate == "none":
        citation = authorname + ". " + pagename + ". " + sitename + ", " + nowtime + ". Web."
    else:
        citation = authorname + ". " + pagename + ". " + sitename + ", " + createdate + ". Web. " + nowtime
    print("Here's your citation! Be sure to italicize the page name in your text editor.")
    print(citation + "\n")
    print("I can write this to a text file. Shall I? Answer with Y/N")
    textchoice = input("")
    if textchoice == "Y" or "y":
        writeCitationToText()
    elif textchoice == "N" or "n":
        print("\n" + "Ah, okay. Good luck with your studies!")
        sys.exit()


if __name__ == '__main__': buildref()