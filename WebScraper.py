import requests
from bs4 import BeautifulSoup
import smtplib,ssl,pushbullet,os,datetime

with open('runlog.txt','a') as f:

    current_time = str(datetime.datetime.now())

    pb = pushbullet.PushBullet(os.environ.get('SECRET_KEY'))

    def log_and_notify(e,current_time=current_time,pb=pb,f=f):
        pb.push_note('Action Error',f'Error: {str(e)}')
        f.write(f'Run Failed: {current_time} Error: {str(e)}\n')
        f.flush()


    try:
        #Get website data
        r_ = requests.get('https://www.playstation.com/en-us/games/hades/')

        #Initialize soup
        soup = BeautifulSoup(r.content,'html.parser')

        #get the price as text and float
        price = soup.find('span',class_="psw-t-title-m").get_text()
        num_price = float(price.strip('$'))

        #compare price to usual price, if cheaper than usual notify me through pushbullet
        if num_price < 24.99:
            pb.push_note('Sale Detected','Sale on Hades detected: ' + price)

        #if succesful add to runlog
        f.write('Run Successful: ' + current_time + ' Price: ' + price + '\n')
        f.flush()

    except Exception as e:
        log_and_notify(e)
