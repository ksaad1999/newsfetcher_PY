"""
    Written by Karim Saad 2018
    Starts the script (main file)
"""
import json
from tkinter import *
URLs = ["https://www.shz.de/lokales/flensburger-tageblatt/rss"]
data = []
for url in URLs:
    functions = __import__("functions")
    data = functions.GetDataFromNews(url=url) #(url="", sFile="")

"""
    UI Stuff
"""
def showData(k): #tkinter F
    print(k["name"], k["date"])
    print(k["text"])

root = Tk()

for item in data:
    button = Button(root, text=item["name"], command=lambda x=item: showData(x))
    button.pack()

root.mainloop()
