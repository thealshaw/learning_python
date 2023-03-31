import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
url = input("Enter URL here\n")
count = input("Enter Count \n")
position = input("Enter Position\n")
if len(count) < 1 and len(position) < 1 :
    count = "7"
    position = "18"
intcount = int(count)
intposition = int(position)
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Blue.html"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")
tags = soup("a")
count2 = 0
count3 = 0
email = list()
while True :  
    for tag in tags :
        email = tag.get("href", None)       
        count3 = count3 + 1
        if count3 == intposition :
            newurl = email
            newdata = urllib.request.urlopen(newurl).read()
            newsoup = BeautifulSoup(newdata, "html.parser")
            tags = newsoup("a") 
            count3 = 0 
            break           
    count2 = count2 + 1
    if count2 == intcount : break
lname = re.findall("_.+_([A-z]+)", email)
name = lname[0]
print("name is", name)


    
    
