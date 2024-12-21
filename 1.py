import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")
print(web.status_code)
# print(web.content)

soup = BeautifulSoup(web.content,"html.parser")

# Tag
tag = soup.html
print(type(tag))

tag = soup.p
print(tag)

# NavigableString
tag = soup.p.string
print(tag)

# Beautifulsoup

print(soup.name)
print(soup.title)
print(soup.body)
   #  soup.body
print(soup.find("h1")) 
line=soup.find_all("p")
for l in line:
    print(l.text) 

# Comments
com =soup.p.string
print(com)
print(soup.body.prettify())

class_data = soup.find("div",class_="why-choose-card")

print(class_data)
print(class_data.find_all("p"))


id_data = soup.find("div",id="s0qs708-aria")
print(id_data)
print(id_data.find_all("p"))



s = soup.find("div",class_="why-choose-card")
lines=s.find_all("p")
for l in lines:
    print(l.text)

for i in soup.find_all("a"):
    print(i.get("href"))    

img=soup.find_all('img')
for i in img:
    print(i.get("src"))
