
import requests
from bs4 import BeautifulSoup 



url= 'https://xkcd.com/353/'

r=requests.get(url)

if r.status_code== 200 :
    print("Successfully opened the web page")
    print("The news are as follow :-\n")
    soup=BeautifulSoup(r.text,"html.parser")
    print(soup.text)
else:
    print("Error")