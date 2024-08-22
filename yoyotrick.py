#Import requestes and beautiful soup
import requests
from bs4 import BeautifulSoup

#get data from trick website
r = requests.get("https://yoyotricks.com/yoyo-tricks/string-tricks/")
soup = BeautifulSoup(r.content,'html.parser')

trick_list = [] #list to store tricks

#get the trick name div's
div_tag = soup.find_all('div',{'class':'caption'})

#grab the  name from the trick div
for tag in div_tag:
    tr = tag.find('h4').get_text()
    trick_list.append(tr)

print(trick_list)