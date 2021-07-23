from re import X, findall
from sys import getprofile
from typing import Text
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.models import Response
import os

# urlList = ['https://clutch.co/profile/unicsoft#reviews','https://clutch.co/profile/tooploox#reviews']
# urlList = ['https://clutch.co/profile/unicsoft#reviews']
web_url =open("final_url.txt" ,"r")
urlList=web_url.read().splitlines()
web_url.close()
# print(urlList)
# rev_total_df =pd.DataFrame(columns = ['Designation & Company Name','Domain','Company Size', 'Location', 'Status', 'Project_Name', 'Project_category','Project_cost','Project_Length','Project_Summary','Review'])
# print('Dataframe:'+rev_total_df)
# rev_total_df.to_csv('rev_total.csv')
# fo = open('rev_total.csv','w')
# fo.write('Designation & Company Name'+','+'Domain','Company Size', 'Location', 'Status', 'Project_Name', 'Project_category','Project_cost','Project_Length','Project_Summary','Review','\n')
# fo.close()
for url in urlList:
    str = url
    a,b = url.split('#',1)
    print(url)

    #response = requests.get(url)
    #print("getting response", response.status_code)

    # while True:
    print('req page')
    response = requests.get(url)
    print("got response", response.status_code)

    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    rev_total = {}
    rev_no = 0

    # reviews = soup.find_all('div',{'class':'view-content main-row'})
    reviews = soup.find_all('div',{'class':'views-row'})
    # print(lists)

    # fo = open('rev_total.csv','a')
    for review in reviews:
        the_reviewer = review.find('div', {'class':'field-name-title'}).find('div', {'class': 'field-item'}).text
        industry = review.find('div', {'class':'field-name-user-industry field-inline custom_popover'}, {'data-content': '<i>Industry</i>'}).find('span').text
        client_size_tag = review.find('div', {'class': 'col-md-3-custom reviewer-col'}).find('div', {'class': 'field-name-company-size field-inline custom_popover'})
        if (client_size_tag != None):
            client_size = client_size_tag.text.strip()
        else:
            client_size = ''


        company_location = review.find('div', {'class': 'col-md-3-custom reviewer-col'}).find('div', {'data-content': '<i>Location</i>'}).text
        # verfication_status = review.find('div', {'class': 'col-md-3-custom reviewer-col'}).find('div', {'data-content': '<i>Not Verified</i>'}).text
        verfication_status = review.find('div', {'class': 'col-md-3-custom reviewer-col'}).find('div', {'class': 'field-name-verified field-inline custom_popover'}).text
        the_project = review.find('h2', {'class': 'h2_title'}).text
        project_category = review.find('div', {'data-content': '<i>Project category</i>'}).find('span').text
        project_cost = review.find('div', {'data-content': '<i>Project size</i>'}).text
        project_length = review.find('div', {'data-content': '<i>Project length</i>'}).text
        project_summary = review.find('div', {'class':'field field-name-proj-description field-inline'}).find('p').text
        the_review = review.find('div', {'class':'field-item'}).find('p').text



        rev_no+=1
        rev_total[rev_no] = [the_reviewer.strip(), industry.strip(), client_size.strip(), company_location.strip(), verfication_status.strip(), the_project.strip(), project_category.strip(), project_cost.strip(), project_length.strip(), project_summary.strip(), the_review.strip()]    


        print("Total Companies:", rev_no)
        rev_total_df = pd.DataFrame.from_dict(rev_total, orient = 'index', columns = ['Designation & Company Name','Domain','Company Size', 'Location', 'Status', 'Project_Name', 'Project_category','Project_cost','Project_Length','Project_Summary','Review'])
        # rev_total_df = pd.DataFrame.from_dict(rev_total)
        # print(rev_total_df) 
    # fo.write(",".join([the_reviewer.strip(), industry.strip(), client_size, company_location.strip(), verfication_status.strip(), the_project.strip(), project_category.strip(), project_cost.strip(), project_length.strip(), project_summary.strip(), the_review.strip(),'\n']))
    # fo.close()
    # x=url.split('#',1)
    rev_total_df.to_csv(os.path.join('companyList', a.split('/')[-1]+'.csv'),index=False)
    print(url)
    url_tag = soup.find('a',{'class': 'page-link'}, {'data-page': ''})
    print(url_tag)
    # if url_tag.get('href'):
    if url_tag is not None:
        url= a + '?' + 'page=' + url_tag.get('data-page')
        print("url:"+url)
    else:
        print('End of page') 


 










