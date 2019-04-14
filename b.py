import requests
from bs4 import BeautifulSoup
x=input("enter the movie name:")

page = requests.get('https://www.rottentomatoes.com/m/'+x.replace(' ','_').lower()).text
soup=BeautifulSoup(page,"html.parser")
article=soup.find('span',class_='mop-ratings-wrap__percentage').text
article2=soup.find('span',class_='mop-ratings-wrap__percentage mop-ratings-wrap__percentage--audience').text
print("critic rating:"+article.strip())
print("audience rating:"+article2.strip())
