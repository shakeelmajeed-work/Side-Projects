import berserk
import requests
import json 
import bs4
from bs4 import BeautifulSoup

#users.json is a file with several keys and the relevant values consisting of things like the user's rating in Blitz and so on.
r = open("users.json","r+")
r = r.read()

r = json.loads(r)
names = []

def prepend(list, str): 
      
    # Using format() 
    str += '{0}'
    list = [str.format(i) for i in list] 
    return(list) 
  
#To get url for each user in team to aid scraping of their tournament points
adder = 'https://lichess.org/@/'
def newUsernames(json_file,user_list):
  for i in range(len(r)):
    user_list.append(json_file[i]['username'])
  names = prepend(user_list, adder)
  return(names)

names = newUsernames(r,names)
print(names)

def pointsScraper(user_list):
  for url in names:
      response = requests.get(url)
      soup = BeautifulSoup(response.content, "html.parser")

      #print titles only
      div = soup.find("div", class_= "number-menu")
      strong = div.find('a', class_='nm-item tournament_stats')
      #i=0
      print(strong.get_text())
      

res = pointsScraper(names)
print(res)


def provisChecker(json_file):
  for i in range(len(r)):
    rating = json_file[i]['perfs']['blitz']['rating']
    if json_file[i]['perfs']['blitz']['games']>=12:
      provis=''
    else:
      provis='PROVISIONAL'
    print(rating,provis)

res = provisChecker(r)
print(res)