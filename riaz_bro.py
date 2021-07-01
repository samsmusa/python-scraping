import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import pandas as pd
import os
headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
Bid_Description = []
Bid_Date = []
html = requests.get('https://vrapp.vendorregistry.com/Bids/View/ExpiredBidsList?buyerId=9e75aac2-0664-4b51-b224-38cb56cddd80')
soup = BeautifulSoup(html.content, "lxml")
bids = soup.find('tbody')

# for bid in bids.find_all("tr"):
#     for td,i in zip(bid.find_all("td"), range(len(bid.find_all("td")))):
#         try:
#             print(i)
#             print(td.text.strip())
#         except :
#             pass
#     print('\\\\\\\\\\\\\\\\/')

for bid in bids.find_all("tr"):
    i = bid.find_all("td")[4]
    try:
        print(i.text.strip())
        
    except :
        pass
