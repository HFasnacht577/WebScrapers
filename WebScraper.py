import requests
from bs4 import BeautifulSoup
import smtplib,ssl,pushbullet,os,datetime

with open('runlog.txt','a') as f:
    current_time = str(datetime.datetime.now())

    pb = pushbullet.PushBullet(os.environ.get('SECRET_KEY'))

    try:
        r = requests.get('https://www.playstation.com/en-us/games/hades/')
    except Exception as e:
        pb.push_note('Action Error','Unable to access game listing')
        f.write('Run Failed: ' + current_time +  ' Error: ' + str(e) + '\n')
        f.flush()
        quit()

    soup = BeautifulSoup(r.content,'html.parser')
    try:
        price = soup.find('span',class_="psw-t-title-m").get_text()
        num_price = float(price.strip('$'))
    except Exception as e:
        pb.push_note('Action Error','Error processing price data')
        f.write('Run Failed: ' + current_time +  ' Error: ' + str(e) + '\n')
        f.flush()
        quit()

    try:
        if num_price < 24.99:
            pb.push_note('Sale Detected','Sale on Hades detected: ' + price)
    except Exception as e:
        pb.push_note('Action Error','Error with price comparison')
        f.write('Run Failed: ' + current_time +  ' Error: ' + str(e) + '\n')
        f.flush()
        quit()

    try:
        f.write('Run Successful: ' + current_time + ' Price: ' + price + '\n')
        f.flush()
    except:
        pb.push_note('Action Error','Unable to write to runlog')