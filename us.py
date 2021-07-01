import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import os

# urlb = 'https://www.thewhiskyexchange.com/search?q=Japanese&pg=2&psize=24'
# url = 'https://www.thewhiskyexchange.com'

headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

links = []
c_name= []


html = requests.get("https://en.wikipedia.org/wiki/List_of_counties_by_U.S._state_and_territory")

soup = BeautifulSoup(html.content, "lxml")
countys  = soup.find_all('div', class_='div-col')


for county in countys:
    for item in county.select("li"):

        name1 = item.get_text().replace(",", "").replace(" ","+")
        reference = "https://www.google.com/search?q=" +  name1 +"+Rfp+Bids"
        
        

        name = item.get_text()

        link ='<a href="{}">{}</a>'.format(reference, name)
        
        links.append(link)
        c_name.append(name)
    

county = {
"Name":c_name,
"googel link": links
}


df = pd.DataFrame(county)
df.to_html(open('uscounty.html', 'w'),escape=False)
