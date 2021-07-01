import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd

headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

#state list
# sate = ["texas","alabama" ]

#data variable list
name_bid = []
region_bid = []
published = []
end = []

#progressbar
pbar = tqdm(total = 100, desc= "Collecting...", unit= "num")

#url
base_url = "https://www.bidnetdirect.com"
# url = "https://www.bidnetdirect.com/alabama/solicitations/open-bids/page1"
url = "https://www.bidnetdirect.com/solicitations/open-bids?selectedContent=AGGREGATE"

#get source of page
def get_data(url):
    html = requests.get(url, headers= headers1)
    soup = BeautifulSoup(html.text, "lxml")

    return soup

#collect data from page
def parse(soup, c):
    content = soup.find('table', class_='mets-table')
    for te in tqdm(content.find_all('tbody'), desc= f'site {c}'):

        rows = te.find_all('tr')
        
        for row in rows:

            name = row.find('a', class_="solicitation-link mets-command-link")
            region = row.find('td', class_='region')
            s_date =  row.find('td', class_='dates publication-date')
            end_date =  row.find('td', class_='dates closing-date')
            
            try:
                name_bid.append(name.text.strip())
                region_bid.append(region.text.strip())
                published.append(s_date.text.strip())
                end.append(end_date.text.strip())
                
            except:
                pass
    
#go next page    
def next_page(soup, base_url):
    next = soup.find("a", class_= "next mets-pagination-page-icon")
    if next:
        url =  base_url + next["href"]
        return url
    else:
        
        return False

c = 1
#main loop = 1
while True:
    
    soup = get_data(url)
    parse(soup, c)
    url = next_page(soup, base_url)
    # print(url)
    pbar.update(1)
    c += 1

    if not  url:
        break

#save data
bid = {
    "name" : name_bid,
    "region": region_bid,
    "Published": published,
    "End": end,
                }
df = pd.DataFrame(bid)
# df.to_html(open('googl11e.html', 'w'),escape=False)
df.to_csv("bid_us.csv")







