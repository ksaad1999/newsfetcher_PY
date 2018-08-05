"""
    Written by Karim Saad 2018
    Starts the script (main file)
"""
import json
from tkinter import *

functions = __import__("functions")
data = functions.GetLinksFromNews()#(url="", sFile="")
for x in data:
    print(x["name"],"\n", x["text"])

d = data
jsonarray = json.dumps(d)
print(jsonarray)

"""
    UI Stuff
"""
def showData(k): #tkinter F
    print(k["name"], k["date"])

root = Tk()

for item in data:
    button = Button(root, text=item["name"], command=lambda x=item: showData(x))
    button.pack()

root.mainloop()
