from os import name
import pandas as pd

from proxy_request import ProxyRequest
from bs4 import BeautifulSoup
from requests.models import encode_multipart_formdata
import os

url = "https://clutch.co/developers/artificial-intelligence"
# file1= open('proxy_list.json','w')
# file1.write(proxy_list.json)
# file1.close()
requests = ProxyRequest()

while True:
    print('req page')
    response = requests.get(url)
    print("got response", response.status_code)
    # with open('index.html', 'w', encoding='utf-8') as f:6 ][]
    #    f.write(response.text)

    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    ## Scrapping Start

    comp_total = {}
    comp_no = 0

    lists = soup.find_all('li',{'class':'provider provider-row sponsor'})
    fo = open("final_url.txt","w")
    # fo.write()
    # fo.close()

    for list in lists:
        
        name = list.find('h3',{'class': 'company_info'}).find('a').text
        rating = list.find('div', {'class': 'rating-reviews'}, {'data-content': 'Avg. hourly rate'}).find('span').text
        Project_size = list.find('div', {'class': 'list-item block_tag custom_popover'}, {'data-content': 'Min. project size'}).find('span').text
        Hourly_rate = list.find('div', {'class': 'list-item custom_popover'}, {'data-content': 'Avg. hourly rate'}).find('span').text
        employees = list.find('div',{'data-content': '<i>Employees</i>'}).find('span').text
        location = list.find('div',{'data-content': '<i>Location</i>'}).find('span', {'class': 'locality'}).text
        focus = list.find('div', {'class': 'carousel-item active'}).text
        link_review= list.find('div',{'class':'reviews-link'}).find('a').get('href')
        # link= list.get('href')
        # print('link')
        
        final_url= 'https://clutch.co'+ link_review
        fo.write(final_url+ '\n')
        # print('final url'+ str(final_url))
        # print("review url link"+str (link_review))

        comp_no+=1
        comp_total[comp_no] = [name, rating, Project_size, Hourly_rate, employees, location, focus, final_url]

    fo.close()   
    url_tag = soup.find('a',{'class': 'page-link'}, {'data-page': ''})

    if url_tag.get('href'):
        url= 'https://clutch.co/developers/artificial-intelligence' + '?' + 'page=' + url_tag.get('data-page') 
    else:
        print('All pages scrapped')
        break


    print("Total Companies:", comp_no)
    comp_total_df = pd.DataFrame.from_dict(comp_total, orient = 'index', columns = ['Company Name','Rating','Project Size', 'Rates', 'No of Employees', 'Location', 'Focus Area','Final url'])
    # print(comp_total_df)

    comp_total_df.to_csv(url_tag.get('data-page')+'.csv')
  
    
