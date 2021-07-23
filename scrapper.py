from re import X, findall
from sys import getprofile
from typing import Text
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests.models import Response
import os

def getReviewDetails(review,rev_no):
    
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
    rev_total[rev_no] = [the_reviewer.strip(), 
                            industry.strip(), 
                            client_size.strip(), 
                            company_location.strip(), 
                            verfication_status.strip(), 
                            the_project.strip(), 
                            project_category.strip(), 
                            project_cost.strip(), 
                            project_length.strip(), 
                            project_summary.strip(), 
                            the_review.strip()]
    return rev_total

def getNextPageReviewDetails(response,rev_no):
    global rev_total_df
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    reviews = soup.find_all('div',{'class':'views-row'})
    for review in reviews:
        rev_no=rev_no+1
        rev_total= getReviewDetails(review,rev_no)
        rev_total_df = pd.DataFrame.from_dict(rev_total, 
                                    orient = 'index', 
                                    columns = ['Designation & Company Name','Domain','Company Size', 'Location', 'Status', 'Project_Name', 'Project_category','Project_cost','Project_Length','Project_Summary','Review'])

        # print("Total Companies:", rev_no)
    rev_total_df.to_csv(os.path.join('companyList', a.split('/')[-1]+'.csv'),index=False)
    return rev_no

web_url =open("final_url.txt" ,"r")
urlList=web_url.read().splitlines()
web_url.close()
# urlList = ['https://clutch.co/profile/unicsoft#reviews']
for url in urlList:
    # str = url
    a,b = url.split('#',1)
    rev_total = {}
    rev_no = 0

    print('Requesting page: {}'.format(url))
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    reviews = soup.find_all('div',{'class':'views-row'})
    for review in reviews:
        rev_no+=1
        rev_total= getReviewDetails(review,rev_no)
        rev_total_df = p(rev_totd.DataFrame.from_dictal, 
                                orient = 'index', 
                                columns = ['Designation & Company Name','Domain','Company Size', 'Location', 'Status', 'Project_Name', 'Project_category','Project_cost','Project_Length','Project_Summary','Review'])
        # print("Total Companies:", rev_no)
    rev_total_df.to_csv(os.path.join('companyList', a.split('/')[-1]+'.csv'),index=False)
    pageNo:int=0
    PageFlag=True
    while PageFlag:
        pageNo=pageNo+1
        nextPageUrl= a +'?' + 'page=' + str(pageNo)  +"#"+ b
        response = requests.get(nextPageUrl)
        firstPageRevNo=rev_no
        rev_no=getNextPageReviewDetails(response, rev_no)
        if firstPageRevNo == rev_no:
            PageFlag=False
        
    print("Total reviews for {} are {}".format(a, rev_no))