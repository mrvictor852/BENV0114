# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:44:10 2023

@author: Victor Chan
"""

#Web Driver Initialisation & URL Input
import pandas as pd
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.set_window_size(700,900)

#AREA 1
#Pier Head
#url = 'https://www.google.com/maps/place/Pier+Head/@53.4045748,-2.9971916,17z/data=!4m7!3m6!1s0x487b212d3b0afab3:0xb6de5921e773521d!8m2!3d53.4045748!4d-2.9971916!9m1!1b1?hl=en'
#Royal Liver Building
#url = ''
#Cunard Building
#url = ''
#Port of Liverpool Building
#url = ''

#AREA 2
#Royal Albert Dock Liverpool
#url = 'https://www.google.com/maps/place/Royal+Albert+Dock+Liverpool/@53.3994337,-2.9919795,17z/data=!3m1!5s0x487b1e7d5e552f79:0x1debce008bba7c8c!4m7!3m6!1s0x487b212bcc348b1f:0xfb50f3d7bf154da9!8m2!3d53.3994337!4d-2.9919795!9m1!1b1?hl=en'
#Canning Dock
#url = 'https://www.google.com/maps/place/Canning+Dock+Liverpool/@53.4013137,-2.9929289,17z/data=!3m1!5s0x487b212b8f0d43db:0x4414f291eeb957cd!4m7!3m6!1s0x487b212c1160a473:0xd7220e07897b4fea!8m2!3d53.4013137!4d-2.9929289!9m1!1b1?hl=en'
#Salthouse Dock
#url = 'https://www.google.com/maps/place/Salthouse+Dock+Liverpool+-+UK/@53.4010682,-2.9927234,17z/data=!4m8!3m7!1s0x487b2162bd163d83:0xf1aa4886bb8ee403!8m2!3d53.4004401!4d-2.9897638!9m1!1b1!16s%2Fg%2F11lkh382n4?hl=en'
#Canning Graving Docks
#url = ''
#Dukes Dock Liverpool
#url = 'https://www.google.com/maps/place/Dukes+Dock+Liverpool/@53.3990189,-2.9912705,18z/data=!4m7!3m6!1s0x487b212a2c3d875d:0x69621eed96babba7!8m2!3d53.3988694!4d-2.9908059!9m1!1b1?hl=en'
#Dukes Dock
#url = 'https://www.google.com/maps/place/Dukes+Dock/@53.3990189,-2.9912705,18z/data=!4m8!3m7!1s0x487b2129833e2d19:0xe5b5cd56cf6bbf46!8m2!3d53.3993639!4d-2.9884604!9m1!1b1!16s%2Fg%2F11b77jky7z?hl=en'
#Canning Half-tide Dock
#url = ''

#AREA 3
#Stanley Dock
#url = 'https://www.google.com/maps/place/Stanley+Dock/@53.4215921,-3.0001884,17z/data=!4m7!3m6!1s0x487b214b224a036f:0x698f99413cdc3530!8m2!3d53.4215921!4d-3.0001884!9m1!1b1?hl=en'
#Stanley Dock North Warehouse
#url = ''
#Stanley Dock Warehouse to south of Tobacco Warehouse
#url = ''
#Victoria Tower
#url = 'https://www.google.com/maps/place/Victoria+Tower/@53.4215248,-3.0049432,17z/data=!4m7!3m6!1s0x487b26b43c5e6479:0x9c4c6bf50bc73fb6!8m2!3d53.4215322!4d-3.0048916!9m1!1b1?hl=en'
#Tobacco Warehouse
#url = 'https://www.google.com/maps/place/Tobacco+Warehouse/@53.4215001,-3.0015504,17z/data=!3m1!5s0x487b214b3ac97059:0x184c8f99b62cdff2!4m8!3m7!1s0x487b236ecc62cb0f:0xd59afe6bf704e8ff!8m2!3d53.4208984!4d-2.9996758!9m1!1b1!16s%2Fg%2F11nxsb3frn?hl=en'


#AREA 4
#Castle Street
#url = ''
#Liverpool Town Hall
#url = 'https://www.google.com/maps/place/Liverpool+Town+Hall/@53.4069438,-2.9915,17z/data=!4m7!3m6!1s0x487b21320069a273:0x6855f5498bb07b07!8m2!3d53.4069438!4d-2.9915!9m1!1b1?hl=en'
#Martins Bank Building
#url = 'https://www.google.com/maps/place/Martins+Bank+Building/@53.4068248,-2.9923375,17z/data=!3m1!5s0x487b212df42a3381:0xa7e50168ac46db49!4m7!3m6!1s0x487b21c67093c909:0xcb3c4ac001954b5f!8m2!3d53.4068248!4d-2.9923375!9m1!1b1?hl=en'
#India Buildings
#url = 'https://www.google.com/maps/place/India+Buildings/@53.406302,-2.993095,17z/data=!3m1!5s0x487b212d858725b7:0xf24c4fbe59a869b2!4m7!3m6!1s0x487b212d930883a1:0xf0227c7f45915e8b!8m2!3d53.406302!4d-2.993095!9m1!1b1?hl=en'
#Oriel Chambers
#url = 'https://www.google.com/maps/place/Oriel+Chambers/@46.3481782,-5.4112154,4z/data=!4m8!3m7!1s0x487b212d91bc50fd:0xd16d04de8e1c7903!8m2!3d53.4069531!4d-2.9936134!9m1!1b1!16s%2Fg%2F12vty2l19?hl=en'

#AREA 5
#William Brown Street
#url = ''
#St George’s Hall
url = "https://www.google.com/maps/place/St+George''s+Hall+Liverpool/@53.40849,-2.9802578,17z/data=!4m7!3m6!1s0x487b212920708c5d:0x3cdad38e75f01dab!8m2!3d53.4080958!4d-2.9804457!9m1!1b1?hl=en"
#World Museum
#url = 'https://www.google.com/maps/place/World+Museum/@53.41,-2.9813889,17z/data=!4m7!3m6!1s0x487b213afc69b5bb:0xef69853bb9fe0239!8m2!3d53.41!4d-2.9813889!9m1!1b1?hl=en'
#Central Library
#url = 'https://www.google.com/maps/place/Central+Library/@53.4100188,-2.9901758,15z/data=!3m1!5s0x487b213b09baaaad:0xc6f63d72aed64045!4m8!3m7!1s0x487b213b05a3aa69:0x5f4ca882f45b6b5d!8m2!3d53.4098392!4d-2.9802884!9m1!1b1!16zL20vMGZfZHQy?hl=en'
#Walker Art Gallery
#url = 'https://www.google.com/maps/place/Walker+Art+Gallery/@53.4100683,-2.9796664,17z/data=!4m7!3m6!1s0x487b213b73ec0249:0xeca81324973ed077!8m2!3d53.4100683!4d-2.9796664!9m1!1b1?hl=en'
#Lime Street Station
#url = 'https://www.google.com/maps/place/Liverpool+Lime+Street/@53.4076217,-2.9773131,17z/data=!4m7!3m6!1s0x487b2124bd7216a5:0xf1b66bcb111ffb4a!8m2!3d53.4076217!4d-2.9773131!9m1!1b1?hl=en'

#AREA 6
#Lower Duke Street
#url = ''
#Bluecoat
#url = 'https://www.google.com/maps/place/The+Bluecoat/@53.40153,-3.0157977,13z/data=!3m1!5s0x487b212dd21472e9:0xe566b496dcc1335c!4m18!1m9!3m8!1s0x487b212587a3287d:0xdc8b09f11abf10ed!2sThe+Bluecoat!8m2!3d53.4041658!4d-2.983863!9m1!1b1!16zL20vMDQwZ3c0!3m7!1s0x487b212587a3287d:0xdc8b09f11abf10ed!8m2!3d53.4041658!4d-2.983863!9m1!1b1!16zL20vMDQwZ3c0?hl=en'
#Royal Institution Bar
#url = 'https://www.google.com/maps/place/Royal+Institution+Bar/@53.4011913,-2.9776611,17z/data=!4m14!1m6!3m5!1s0x487b210008ae0265:0x1374ed62b03e607a!2sRoyal+Institution+Bar!8m2!3d53.4012439!4d-2.9777294!3m6!1s0x487b210008ae0265:0x1374ed62b03e607a!8m2!3d53.4012439!4d-2.9777294!9m1!1b1?hl=en'
#Old Bridewell
#url = ''

#Navigating
driver.get(url)
driver.find_element("xpath", '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div[1]/div/button').click()
##to make sure content is fully loaded we can use time.sleep() after navigating to each page
time.sleep(3)

#Select sorting perference
driver.find_element("xpath", "//button[@data-value='Sort']").click()
time.sleep(1)
#most relevant (default)
driver.find_element("xpath", '//*[@id="action-menu"]/div[1]').click()
#newest
#driver.find_element("xpath", '//*[@id="action-menu"]/div[2]').click()
#highest rating
#driver.find_element("xpath", '//*[@id="action-menu"]/div[3]').click()
#lowest rating
#driver.find_element("xpath", '//*[@id="action-menu"]/div[4]').click()
time.sleep(5)

#Scrolling and Loading More Reviews
#Find the total number of reviews
total_number_of_reviews = driver.find_element("xpath", '//*[@class="fontBodySmall"]').text.split(" ")[0]

total_number_of_reviews = int(total_number_of_reviews.replace(',','')) if ',' in total_number_of_reviews else int(total_number_of_reviews)

#Find scroll layout
scrollable_div = driver.find_element("xpath", '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')

#Scroll as many times as necessary to load all reviews
###################You may adjust the time for scrolling here#########################################
#Scroll 200 times
for c in range(0,180):
#Scroll according to the number of reviews
#for c in range(0,(round(total_number_of_reviews/10 + 1))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                scrollable_div)
        time.sleep(1)
#######################################################################################################

#Parsing HTML and Data Extraction
item = driver.find_element("xpath", '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]')

time.sleep(3)

#Create variable list
name_list = []
stars_list = []
review_list = []
duration_list = []

#Click "More" for all the reviews
#for i in item:
button = item.find_elements("xpath", '//*[@class="w8nwRe kyuRq"]')

for m in button:
    if m.text == "More":
        m.click()

time.sleep(3)

#Obtain the variable values
name = item.find_elements("xpath", '//*[@class="d4r55"]')
stars = item.find_elements("xpath", '//*[@class="kvMYJc"]')
review = item.find_elements("xpath", '//*[@class="wiI7pd"]')
duration = item.find_elements("xpath", '//*[@class="rsqaWe"]')

#Save the values into the list
for j,k,l,p in zip(name,stars,review,duration):
    name_list.append(j.text)
    duration_list.append(p.text)
    stars_list.append(k.get_attribute("aria-label"))
    review_list.append(l.text)

#Make dataset
review = pd.DataFrame(
    {'name': name_list,
     'rating': stars_list,
     'review': review_list,
     'duration': duration_list})

#Save to csv
review.to_csv('google_review.csv',index=False)
print(review)