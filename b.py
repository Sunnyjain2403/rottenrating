import requests
from bs4 import BeautifulSoup
x=input("enter the movie(*no letter in capital):")
page = requests.get('https://www.rottentomatoes.com/m/'+x).text
soup=BeautifulSoup(page,"html.parser")
article=soup.find('span',class_='mop-ratings-wrap__percentage').text
article2=soup.find('span',class_='mop-ratings-wrap__percentage mop-ratings-wrap__percentage--audience').text
print("critic rating:"+article)
print("audience  rating"+article2)


