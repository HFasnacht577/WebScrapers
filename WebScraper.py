import requests
from bs4 import BeautifulSoup
import smtplib,ssl,pushbullet,os

pb = pushbullet.PushBullet(os.environ.get('SECRET_KEY'))
try:
    r = requests.get('https://www.playstation.com/en-us/games/hades/')
except:
    pb.push_note('Action Error','Unable to access game listing')
    quit()

soup = BeautifulSoup(r.content,'html.parser')
try:
    s = soup.find('span',class_="psw-t-title-m").get_text()
    s_clean = float(s.strip('$'))
except:
    pb.push_note('Action Error','Error retrieving and processing price data')
    quit()

try:
    if s_clean < 24.99:
        pb.push_note('Sale Detected','Sale on Hades detected: ' + s)
        quit()
except:
    pb.push_note('Action Error','Error with sale detection submission.')
    quit()
