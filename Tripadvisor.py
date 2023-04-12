# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:55:34 2023

@author: Victor Chan
"""

##########START HERE###############
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
import time

# open Firefox (you may need to install Firefox first)
browser = webdriver.Firefox()
browser.set_window_size(700,900)

# create dataframe (clear all data saved in df)
df = pd.DataFrame(columns = ['user','bubbles','country','contributions','title','description','date','link'])

# change the link here:
############################################################################################################################################################
#AREA 2
#Royal Albert Dock Liverpool
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d189273-Reviews-Royal_Albert_Dock_Liverpool-Liverpool_Merseyside_England.html"
#Canning Dock
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d19516277-Reviews-Canning_Dock-Liverpool_Merseyside_England.html"
#Salthouse Dock#
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d19525550-Reviews-Salthouse_Dock-Liverpool_Merseyside_England.html"
#Canning Graving Docks
#NO SUCH PAGE#
#Duke's Dock
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d20322713-Reviews-Duke_s_Dock-Liverpool_Merseyside_England.html"
#Canning Half-tide Dock
#NO SUCH PAGE#
#Albert Dock
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d11813027-Reviews-Albert_Dock-Liverpool_Merseyside_England.html"

#AREA 3
#Stanley Dock
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d23116078-Reviews-Stanley_Dock-Liverpool_Merseyside_England.html"
#Tobacco Warehouse Building
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d23116075-Reviews-Tobacco_Warehouse_Building-Liverpool_Merseyside_England.html"
#Victoria Tower
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d23116080-Reviews-Victoria_Tower-Liverpool_Merseyside_England.html"

#AREA 4
#Castle Street
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d21249205-Reviews-Castle_Street-Liverpool_Merseyside_England.html"
#Martins Building
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d21173214-Reviews-Martins_Building-Liverpool_Merseyside_England.html"
#India Buildings
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d12959332-Reviews-India_Buildings-Liverpool_Merseyside_England.html"
#Oriel Chambers Building
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d23118571-Reviews-Oriel_Chambers_Building-Liverpool_Merseyside_England.html"

#AREA 5
#William Brown Street
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d20991992-Reviews-William_Brown_Street-Liverpool_Merseyside_England.html"
#St George’s Hall
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d207708-Reviews-St_George_s_Hall-Liverpool_Merseyside_England.html"
#World Museum
url = "https://www.tripadvisor.com/Attraction_Review-g186337-d215399-Reviews-World_Museum-Liverpool_Merseyside_England.html"
#Liverpool Central Library
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d215392-Reviews-Liverpool_Central_Library-Liverpool_Merseyside_England.html"
#Walker Art Gallery
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d213957-Reviews-Walker_Art_Gallery-Liverpool_Merseyside_England.html"
#Lime Street Railway Station
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d6206910-Reviews-Lime_Street_Railway_Station-Liverpool_Merseyside_England.html"

#AREA 6
#Old Bridewell Prison Building
#url = "https://www.tripadvisor.com/Attraction_Review-g186337-d21153366-Reviews-Old_Bridewell_Prison_Building-Liverpool_Merseyside_England.html"
############################################################################################################################################################

# grab the information (user name, country, contributions, review title, and content) for each review in each page (10 reviews per page)
browser.get(url)
time.sleep(4) #adjust loding time in second(s)
response = browser.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(response, 'lxml')
for review in soup.find_all('div', {'data-automation': 'reviewCard'}):
    data = [data.getText() for data in review.find_all('span') if data.getText()]
    user = data[0]
    if 'contribution' in data[1]:
        country = 'No Country'
        contributions = data[1]
        title = data[4]
        description = data[5]
    elif 'Read more' in data[5]:
        country = 'No Country'
        contributions = '0'
        title = data[3]
        description = data[4]
    elif 'Read more' in data[6]:
        country = data[1]
        contributions = '0'
        title = data[4]
        description = data[5]
    else:
        country = data[1]
        contributions = data[2]
        title = data[5]
        description = data[6]

# grab the rating
    bubbles = [bubble.get('aria-label') for bubble in review.find_all('svg') if bubble.has_attr('aria-label')][0]

# grab the date    
    data2 = [data2.getText() for data2 in review.find_all('div') if data2.getText()]
    if 'Written' in data2[13]:
        date = data2[13]
    elif 'Written' in data2[12]:
        date = data2[12]
    else:
        date = data2[15]
        
    if 'contribution' in data2[3] and contributions == '0':
        contributions = data2[3]
    else:
        contributions = data2[5]
        
# grab the individual review link        
    link = ['https://www.tripadvisor.com', review.find_all("a", {"target": "_blank"})[0]['href']]
    link = ''.join(link)

# combine all the information into a list    
    list = [user, bubbles, country, contributions, title, description, date, link]
# save the list to the last row of dataframe
    df = df.append(pd.Series(list, index = ['user','bubbles','country','contributions','title','description','date','link']), ignore_index=True)

 

# please change the 'middle' number according to the last page number of the reviews':
##############################################################################
#Royal Albert Dock Liverpool
#for x in range(10, 15890, 10):
#Albert Dock
#for x in range(10, 270, 10):
#St. George's Hall
#for x in range(10, 1540, 10):
#World Museum
for x in range(10, 3280, 10):
#Liverpool Central Library
#for x in range(10, 1730, 10):
#Walker Art Gallery
#for x in range(10, 2230, 10):
#Lime Street Railway Station
#for x in range(10, 960, 10):
##############################################################################
 
# change and split the link here:
###################################################################################################################################################################################################
#Royal Albert Dock Liverpool
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d189273-Reviews-or', str(x), '-Royal_Albert_Dock_Liverpool-Liverpool_Merseyside_England.html']
#Albert Dock
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d11813027-Reviews-or', str(x), '-Albert_Dock-Liverpool_Merseyside_England.html']
#St. George's Hall
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d207708-Reviews-or', str(x), '-St_George_s_Hall-Liverpool_Merseyside_England.html']
#World Museum
    url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d215399-Reviews-or', str(x), '-World_Museum-Liverpool_Merseyside_England.html']
#Liverpool Central Library
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d215392-Reviews-or', str(x), '-Liverpool_Central_Library-Liverpool_Merseyside_England.html']
#Walker Art Gallery
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d213957-Reviews-or', str(x), '-Walker_Art_Gallery-Liverpool_Merseyside_England.html']
#Lime Street Railway Station
    #url_list = ['https://www.tripadvisor.com/Attraction_Review-g186337-d6206910-Reviews-or', str(x), '-Lime_Street_Railway_Station-Liverpool_Merseyside_England.html']
###################################################################################################################################################################################################
    url = ''.join(url_list)
  
# grab the information (user name, country, contributions, review title, and content) for each review in each page (10 reviews per page)
    browser.get(url)
    time.sleep(4) #adjust loding time in second(s)
    response = browser.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(response, 'lxml')
    for review in soup.find_all('div', {'data-automation': 'reviewCard'}):
        data = [data.getText() for data in review.find_all('span') if data.getText()]
        user = data[0]
        if 'contribution' in data[1]:
            country = 'No Country'
            contributions = data[1]
            title = data[4]
            description = data[5]
        elif 'Read more' in data[5]:
            country = 'No Country'
            contributions = '0'
            title = data[3]
            description = data[4]
        elif 'Read more' in data[6]:
            country = data[1]
            contributions = '0'
            title = data[4]
            description = data[5]     
        else:
            country = data[1]
            contributions = data[2]
            title = data[5]
            description = data[6]

# grab the rating
        bubbles = [bubble.get('aria-label') for bubble in review.find_all('svg') if bubble.has_attr('aria-label')][0]

# grab the date    
        data2 = [data2.getText() for data2 in review.find_all('div') if data2.getText()]
        if 'Written' in data2[13]:
            date = data2[13]
        elif 'Written' in data2[12]:
            date = data2[12]
        else:
            date = data2[15]
        
        if 'contribution' in data2[3] and contributions == '0':
            contributions = data2[3]
        else:
            contributions = data2[5]
        
# grab the individual review link        
        link = ['https://www.tripadvisor.com', review.find_all("a", {"target": "_blank"})[0]['href']]
        link = ''.join(link)

# combine all the information into a list    
        list = [user, bubbles, country, contributions, title, description, date, link]
# save the list to the last row of dataframe
        df = df.append(pd.Series(list, index = ['user','bubbles','country','contributions','title','description','date','link']), ignore_index=True)




# save the dataframe into csv file. please check where the file would be saved.
df.to_csv('out.csv', encoding='utf-8')
