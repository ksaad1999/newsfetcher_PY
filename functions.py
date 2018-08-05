"""
Written by Karim Saad 2018
"""

def GetPage(url):
    try:
        import requests
        html_doc = requests.get(url).content
        return html_doc
    except Exception as e:
        print(e)

def Write2File(fn="out.txt", text=""):
    try:
        f = open(fn,"w")
        f.write(text)
        f.close()
        return True
    except Exception as e:
        print (e)
        return False

def EscapeText(text):
    return text.replace("\t","").replace("\r","").replace("\n", "")

def GetDataFromNews(url="https://www.shz.de/lokales/flensburger-tageblatt/rss", sFile="meldungen_flensburg.txt"):
    import feedparser, json
    feed = feedparser.parse( url )
    n = feed[ "items" ]
    data = []
    for x in n:
        try:
            ax = {"name": x["title"], "url": x["link"], "date":x['published'], "text": x["text"].replace("<p>","").replace("&uuml","ü").replace("&ouml","ö").replace("</p>","").replace("&auml","ä").replace("<br>","").replace("</br>","").replace("<br />","").replace("ä;","ä").replace("&szlig;","ß").replace("ü;","ü").replace("&Uuml","Ü").replace("Ü;","Ü").replace("ö;","ö")}
            data.append(ax)
        except Exception as e:
            print("key not found:\t", e)
            continue
    jsonarray = json.dumps(data)
    Write2File(sFile, str(jsonarray))
    return data
