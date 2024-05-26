import requests
from bs4 import BeautifulSoup
import smtplib,ssl,pushbullet

r = requests.get('https://www.playstation.com/en-us/games/hades/')


soup = BeautifulSoup(r.content,'html.parser')

s = soup.find('span',class_="psw-t-title-m").get_text()

s_clean = float(s.strip('$'))

if s_clean == 24.99:
    pb = pushbullet.PushBullet(secret_key)   pb.push_note('Sale Detected','Sale on Hades detected: ' + s)
