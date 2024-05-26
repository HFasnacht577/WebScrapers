import requests
from bs4 import BeautifulSoup
import smtplib,ssl,pushbullet,os

pb = pushbullet.PushBullet(os.environ.get('SECRET_KEY')
try:
    r = requests.get('https://www.playstation.com/en-us/games/hades/')
except:
    pb.push_note('Action Error','Unable to access game listing')
    return

soup = BeautifulSoup(r.content,'html.parser')
try:
    s = soup.find('span',class_="psw-t-title-m").get_text()
    s_clean = float(s.strip('$'))
except:
    pb.push_note('Action Error','Error retrieving and processing price data')
    return

try:
    if s_clean == 24.99:
        pb.push_note('Sale Detected','Sale on Hades detected: ' + s)
        return
except:
    pb.push_note('Action Error','Error with sale detection submission.')
    return
