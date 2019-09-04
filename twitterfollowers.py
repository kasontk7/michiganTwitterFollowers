from bs4 import BeautifulSoup
import requests
import csv

twurl = "https://www.twitter.com/"
handles = [
"umichbaseball",
"umichbball",
"umichwbball",
"umichtrack",
"umichfldhockey",
"umichfootball",
"umichgolf",
"umichgym",
"umichwgym",
"umichhockey",
"umichlacrosse",
"umichwlax",
"umichrowing",
"umichsoccer",
"umichwsoccer",
"umichsoftball",
"umichswimdive",
"umichtennis",
"umichwtennis",
"umichtrack",
"umichvball",
"umichwaterpolo",
"umichwrestling",
"umichathletics"
]
fburl = "https://www.facebook.com/"
fbs = [
"MichiganBaseball",
"MichiganBasketball",
"michiganwomensbasketball",
"michiganmenstrack",
"michiganwomenstrack",
"michiganfieldhockey",
"michiganfball",
"MichiganGolf",
"michiganwomensgolf",
"MichiganMensGymnastics",
"MichiganGymnastics",
"MichiganHockey",
"MichiganMensLacrosse",
"MichiganWomensLacrosse",
"michiganrowing",
"michigansoccer",
"michiganwsocc",
"MichiganSoftball",
"michiganmensswimming",
"michiganwomensswimming",
"MichiganTennis",
"UofMTennis",
"michiganmenstrack",
"michiganwomenstrack",
"MichiganVolleyball",
"michiganwpolo",
"michiganwrestling",
"umichathletics"
]

# igurl = "https://www.instagram.com/"
# igs = [
# "umichbaseball",
# "umichbball",
# "umichwbball",
# "umichdance",
# "umichfieldhockey",
# "umichfootball",
# "umichgolf", 
# "umichgym",
# "umichwgym",
# "umichhockey",
# "umichlacrosse",
# "umichwlax",
# "umichrowing",
# "umichsoccer",
# "umichwsoccer",
# "umichsoftball",
# "umichswimdive",
# "umichmtennis",
# "umichwtennis",
# "umichtrack",
# "umichvball",
# "umichwaterpolo",
# "umichwrestling",
# "umichathletics"
# ]

header = ["Platform", "Account", "Followers"]
with open('followers.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)

for handle in handles:
    page = requests.get(twurl+handle)
    soup = BeautifulSoup(page.content, 'html.parser')
    doc = soup.find("div", id="doc") #, class_='ProfileNav-value')
    followers = doc.find("li", class_="ProfileNav-item ProfileNav-item--followers")
    value = followers.find("span", class_="ProfileNav-value")
    data = []
    data.append("Twitter")
    data.append(handle)
    data.append(value['data-count'])
    print(data)
    with open('followers.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)

for fb in fbs:
    page = requests.get(fburl+fb)
    soup = BeautifulSoup(page.content, 'html.parser')
    list1 = soup.find_all("div", class_="_2pi9 _2pi2")
    followstring = list1[1].find("div", class_="_4bl9")
    followers = followstring.get_text().split(" ")[0]
    data = []
    data.append("Facebook")
    data.append(fb)
    data.append(followers)
    print(data)
    with open('followers.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(data)
