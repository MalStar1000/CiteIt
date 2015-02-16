import time
from datetime import datetime
import sys
import os.path
global authorname
global pagename
global sitename
global createdate
global citation

def intro():
    print("CiteIt - MLA Web Citation Creator - By Meorge\n")
    ask()

def ask():
    print("What kind of refrence would you like to make?\nAnswer with \"web\" or \"book\".")
    askchoice = input("")
    if askchoice == "web" or askchoice == "Web":
        buildrefWeb()
    elif askchoice == "book" or askchoice == "Book":
        buildrefBook()
    else:
        print("Sorry, I don't understand. Please try again.")
        sys.exit()

def buildrefWeb():
    global authorname
    global pagename
    global sitename
    global createdate
    print("\nType the author's name here in Last, First format (example: \"Jobs, Steve\").")
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
    createcitationWeb()

def buildrefBook():
    global authorname
    global transchoice
    global translatorname
    global bookname
    global pubcity
    global pubname
    global bookyear
    global istranslated
    print("\nType the author's name here in Last, First format. (example: \"Jobs, Steve\").")
    authorname = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Was the book translated by anyone? Answer with Y/N.")
    transchoice = input("")
    if transchoice == "y" or "Y":
        istranslated = True
        print("\n\nType the translator's name here in First Last format (example: \" Robert Fitzgerald\").")
        translatorname = input("")
        print("Recording...")
        time.sleep(3)
        print("\n\n")
    elif transchoice == "n" or "N":
        istranslated = False
    print("Type the book's name here (example: \"Great Poets of tbe 19th Century\").")
    bookname = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the city of publication's name here (example: \"Boston\").")
    pubcity = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the publisher's name here (example: \"Penguin Books\".)")
    pubname = input("")
    print("Recording...")
    time.sleep(3)
    print("\n\n")
    print("Type the year of the publication (example: \"1992\").")
    bookyear = input("")
    print("Recording...")
    time.sleep(3)
    createcitationBook()


def createcitationWeb():
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
        if os.path.isfile("works-cited.txt"):
            fo = open('works-cited.txt', 'a')
            fo.write("\n" + citation)
            fo.close
            print("Your Works Cited document has been updated with your citation!")
        else:
            fo = open('works-cited.txt', 'w')
            fo.write("Works Cited\n" + citation)
            fo.close
            print("A text file in the same directory as this program has been generated with your citation.\nYou can re-run this script and add more citations to it.\nThe file is called \"works-cited.txt\".")
    elif textchoice == "N" or "n":
        print("\n" + "Ah, okay. Good luck with your studies!")
        sys.exit()

def createcitationBook():
    global authorname
    global transchoice
    global translatorname
    global bookname
    global pubcity
    global pubname
    global bookyear
    global istranslated
    global citation
    print("Now working on your citation...")
    time.sleep(4)
    if istranslated == True:
        citation = authorname + ". Trans: " + translatorname + ". " + bookname + ". " + pubcity + ": " + pubname + ", " + bookyear + ". Print."
    else:
        citation = authorname + ". " + bookname + ". " + pubcity + ": " + pubname + ", " + bookyear + ". Print."
    print("Here's your citation! Be sure to italicize the page name in your text editor.")
    print(citation + "\n")
    print("I can write this to a text file. Shall I? Answer with Y/N")
    textchoice = input("")
    if textchoice == "Y" or "y":
        if os.path.isfile("works-cited.txt"):
            fo = open('works-cited.txt', 'a')
            fo.write("\n" + citation)
            fo.close
            print("Your Works Cited document has been updated with your citation!")
        else:
            fo = open('works-cited.txt', 'w')
            fo.write("Works Cited\n" + citation)
            fo.close
            print("A text file in the same directory as this program has been generated with your citation.\nYou can re-run this script and add more citations to it.\nThe file is called \"works-cited.txt\".")
    elif textchoice == "N" or "n":
        print("\n" + "Ah, okay. Good luck with your studies!")
        sys.exit()

    '''if os.path.isfile("works-cited.txt"):
        fo = open('works-cited.txt', 'a')
        fo.write("\n" + citation)
        fo.close
        print("Your Works Cited document has been updated with your citation!")
    else:
        fo = open('works-cited.txt', 'w')
        fo.write("Works Cited\n" + citation)
        fo.close
        print("A text file in the same directory as this program has been generated with your citation.\nYou can re-run this script and add more citations to it.\nThe file is called \"works-cited.txt\".")'''


if __name__ == '__main__': intro()