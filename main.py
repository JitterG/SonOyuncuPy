# main.py
from bs4 import BeautifulSoup
import requests
 
def gswusername(username,game,time = None):
    if time is None:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game)
    else:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game+"/"+time)
    soup = BeautifulSoup(sonoyuncuWebsite.text, "html.parser")

    users = []

    siralamanick = soup.findAll("td", attrs={"class":"text-left py-3"})
    siralamapuan = soup.findAll("td", attrs={"class":"text-right pr-6"})

    for i, (nick, puan) in enumerate(zip(siralamanick, siralamapuan), start=1):
        users.append({"siralama": f"{i}.", "nickname": nick.text.strip(), "score": puan.text.strip()})

    for user in users:
        if user["nickname"] == username:
            return {"username": username, "siralama": user["siralama"], "score": user["score"]}
    
    return {"error": "User not found"}

def gswrank(rank,game,time = None):
    if time is None:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game)
    else:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game+"/"+time)
    soup = BeautifulSoup(sonoyuncuWebsite.text, "html.parser")

    users = []

    siralamanick = soup.findAll("td", attrs={"class":"text-left py-3"})
    siralamapuan = soup.findAll("td", attrs={"class":"text-right pr-6"})

    for i, (nick, puan) in enumerate(zip(siralamanick, siralamapuan), start=1):
        users.append({"siralama": f"{i}.", "nickname": nick.text.strip(), "score": puan.text.strip()})

    for user in users:
        if user["siralama"] == rank:
            return {"username": user["nickname"], "siralama": user["siralama"], "score": user["score"]}
    
    return {"error": "Rank not found"}

def listrank(game,time = None):
    if time is None:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game)
    else:
        sonoyuncuWebsite = requests.get("https://sonoyuncu.com.tr/siralamalar/"+game+"/"+time)
    soup = BeautifulSoup(sonoyuncuWebsite.text, "html.parser")

    users = []

    siralamanick = soup.findAll("td", attrs={"class":"text-left py-3"})
    siralamapuan = soup.findAll("td", attrs={"class":"text-right pr-6"})

    for i, (nick, puan) in enumerate(zip(siralamanick, siralamapuan), start=1):
        users.append({"username": nick.text.strip(),"siralama": f"{i}.","score": puan.text.strip()})

    try:
        return users

    except:
        return {"error": "List not found"}

x = listrank("thebridge","2023")
for user in x:
    print(user['siralama']+user['username'])