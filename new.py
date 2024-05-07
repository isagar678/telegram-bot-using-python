from bs4 import BeautifulSoup
import requests
import json
def headliners(category):
    url =f"https://www.hindustantimes.com/{category}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        soup = BeautifulSoup(response.text,'html.parser')
        news_report = soup.find_all('h2')
        for i in news_report:
            print("--> ",i.get_text().strip())
print("News Headlines")
with open('intents.json') as j :
    loader =json.load(j)
    for i in loader['category']:
        print(i,end=" ")
str1 = str(input("Enter Category from above ")).lower()
if str1 in loader['category']:
    headliners(str1)
else :
    print("selected category is not available")

