from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
base_url = "https://www.apartments.com/newton-ma/"
r =  requests.get(base_url, headers=headers)
# print(page.text)
#
soup = bs(r.text, 'html.parser')
# print(soup)

paging = soup.find('div',{'id': 'paging'}).findAll('a')
start_page = paging[1].text
last_page = paging[len(paging)-2].text

web_content_list = []

for page_number in range(int(start_page),int(last_page)+1):
    url = base_url+str(page_number)+'/'
    r = requests.get(url, headers=headers)
    soup = bs(r.text, 'html.parser')
    # print(soup,'\n\n\n\n\n\n\n')

    placard_header = soup.find_all('header', {'class': 'placardHeader'})
    placard_content = soup.find_all('section', {'class':'placardContent'})

    # print(placard_header)

    for item_header,item_content in zip(placard_header,placard_content):
        web_content_dict = {}
        web_content_dict["Title"] = item_header.find("a", {"class": "placardTitle"}).text.replace("\r","").replace("\n", "")
        web_content_dict["Address"] = item_header.find("div",{"class":"location"}).text
        web_content_dict["Price"] = item_content.find("span",{"class":"altRentDisplay"}).text
        web_content_dict["Beds"] = item_content.find("span",{"class":"unitLabel"}).text
        web_content_dict["Phone"] = item_content.find("div",{"class":"phone"}).find("span").text
        link = [str(i["href"]) for i in item_header.find_all("a", {"href": True})]
        web_content_dict["Link"] = link[0]

        web_content_list.append(web_content_dict)
# print(web_content_list)
df = pd.DataFrame(web_content_list)
df.to_csv('/Users/urieldabby/Downloads/apartments.csv')