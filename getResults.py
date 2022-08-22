from gc import collect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time
import requests
import json

def putInFilters(data, driver):
    print(data)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body/yelp-react-root[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/ul[1]/li[4]/div[1]/div[1]/span[1]/div[1]/button[1]"))).click()
    time.sleep(.5)
    #open filters
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/yelp-react-root/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[3]/p/a"))).click()
    time.sleep(.5)
    
    for value in data['checkboxInput']:
        if value == '1': #vegetarian
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body[1]/yelp-react-root[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[5]/label[1]/div[1]/div[1]"))).click()
        if value == '2': #delivery
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body[1]/yelp-react-root[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[13]/label[1]/div[1]/div[1]/input[1]"))).click()
        if value == '3': #kids
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body[1]/yelp-react-root[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[10]/label[1]/div[1]/div[1]/input[1]"))).click()
    
    #apply filters
    driver.find_element_by_css_selector("div.overlay__09f24__uZ4r5 div.modal__09f24__EJkd3.hiddenOverflow__09f24___ai7N.medium__09f24__qAxVk div.modal-body__09f24__W_lm_.border-color--default__09f24__NPAKY div.margin-t3__09f24__riq4X.border-color--default__09f24__NPAKY.text-align--right__09f24__VXn6f button.css-1n9j64s > span.css-1enow5j").click()
    time.sleep(1)


    for value in data['price']:
        if value == '4':
            driver.find_element_by_css_selector("div.popover__09f24__Git7B.border-color--default__09f24__NPAKY div.popoverInner__09f24__Ii5R2.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.filterPanelWrapper__09f24__yHStf.margin-b7__09f24__bfwvv.padding-l5__09f24__IQ8Wp.border-color--default__09f24__NPAKY div.container__09f24__OorIL.bottomAligned__09f24__F6LJ_.margin-r5__09f24__s1_FL.padding-t4__09f24__Y6aGL.border-color--default__09f24__NPAKY div.padding-t2__09f24__Y6duA.padding-b2__09f24__F0z5y.border--bottom__09f24___mg5X.border-color--default__09f24__NPAKY:nth-child(4) div.verticalLayout__09f24__kw_cU.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.growContainer__09f24__Rm95E.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY > button.filterToggle__09f24__gyiyZ.growFilter__09f24__SJOGc.leftRounded__09f24__vfVNj.noRightBorder__09f24__dMmus.growFilterContainer__09f24__ZeedZ.css-1fygppl:nth-child(1)").click()
        if value == '5':
            driver.find_element_by_css_selector("div.popover__09f24__Git7B.border-color--default__09f24__NPAKY div.popoverInner__09f24__Ii5R2.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.filterPanelWrapper__09f24__yHStf.margin-b7__09f24__bfwvv.padding-l5__09f24__IQ8Wp.border-color--default__09f24__NPAKY div.container__09f24__OorIL.bottomAligned__09f24__F6LJ_.margin-r5__09f24__s1_FL.padding-t4__09f24__Y6aGL.border-color--default__09f24__NPAKY div.padding-t2__09f24__Y6duA.padding-b2__09f24__F0z5y.border--bottom__09f24___mg5X.border-color--default__09f24__NPAKY:nth-child(4) div.verticalLayout__09f24__kw_cU.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.growContainer__09f24__Rm95E.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY > button.filterToggle__09f24__gyiyZ.growFilter__09f24__SJOGc.noRightBorder__09f24__dMmus.growFilterContainer__09f24__ZeedZ.css-1fygppl:nth-child(2)").click()
            driver.find_element_by_css_selector("div.popover__09f24__Git7B.border-color--default__09f24__NPAKY div.popoverInner__09f24__Ii5R2.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.filterPanelWrapper__09f24__yHStf.margin-b7__09f24__bfwvv.padding-l5__09f24__IQ8Wp.border-color--default__09f24__NPAKY div.container__09f24__OorIL.bottomAligned__09f24__F6LJ_.margin-r5__09f24__s1_FL.padding-t4__09f24__Y6aGL.border-color--default__09f24__NPAKY div.padding-t2__09f24__Y6duA.padding-b2__09f24__F0z5y.border--bottom__09f24___mg5X.border-color--default__09f24__NPAKY:nth-child(4) div.verticalLayout__09f24__kw_cU.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.growContainer__09f24__Rm95E.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY > button.filterToggle__09f24__gyiyZ.growFilter__09f24__SJOGc.noRightBorder__09f24__dMmus.growFilterContainer__09f24__ZeedZ.css-1fygppl:nth-child(3)").click()
        if value == '6':
            driver.find_element_by_css_selector("div.popover__09f24__Git7B.border-color--default__09f24__NPAKY div.popoverInner__09f24__Ii5R2.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.filterPanelWrapper__09f24__yHStf.margin-b7__09f24__bfwvv.padding-l5__09f24__IQ8Wp.border-color--default__09f24__NPAKY div.container__09f24__OorIL.bottomAligned__09f24__F6LJ_.margin-r5__09f24__s1_FL.padding-t4__09f24__Y6aGL.border-color--default__09f24__NPAKY div.padding-t2__09f24__Y6duA.padding-b2__09f24__F0z5y.border--bottom__09f24___mg5X.border-color--default__09f24__NPAKY:nth-child(4) div.verticalLayout__09f24__kw_cU.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY div.border-color--default__09f24__NPAKY div.growContainer__09f24__Rm95E.display--inline-block__09f24__fEDiJ.border-color--default__09f24__NPAKY > button.filterToggle__09f24__gyiyZ.growFilter__09f24__SJOGc.rightRounded__09f24___p0ah.growFilterContainer__09f24__ZeedZ.css-1fygppl:nth-child(4)").click()
    #apply filters
    driver.find_element_by_xpath("//body[1]/yelp-react-root[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]").click()
    time.sleep(1)

def inputQuery(data, driver):
    #search
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_description"))).send_keys(Keys.CONTROL, 'a')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_description"))).send_keys(Keys.BACKSPACE)
    driver.find_element_by_css_selector("#search_description").send_keys(data['type'])
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_location"))).send_keys(Keys.CONTROL, 'a')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_location"))).send_keys(Keys.BACKSPACE)
    driver.find_element_by_css_selector("#search_location").send_keys(str(data['zip']))
    driver.find_element_by_css_selector("#search_location").send_keys(Keys.ENTER)
    

def compileResults(driver):
    #instantiate beautfiul soup
    url = driver.current_url
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    finalRestaurantList = []
    page_text = doc.find_all(class_="css-1m051bw")
    for element in page_text:
        title = element.get_text()
        finalRestaurantList.append(title)
    return finalRestaurantList

def searchRestaurant(restaurant, zip, driver):
    driver.get("https://google.com")
    element = driver.find_element_by_xpath('//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
    element.send_keys(str(restaurant) + ' ' + str(zip))
    element.submit()

def collectPageDataOnLoad(driver):
    time.sleep(.5)
    url = driver.current_url
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    f = soup.find_all('span')
    count = 'uncounted'
    address= None
    rating= None
    hours= None
    phone = None
    for index, word in enumerate(f):
        if word.string == "Rating" and count == 'uncounted':
            rating = f[index+2].string
            count == 'counted'
        elif word.string == "Address":
            address = f[index+1].string
        elif word.string == "Hours":
            hours = f[index+1].string
        elif word.string == "Phone":
            phone = f[index+1].string
    macroData = {
        'rating' : rating,
        'address' : address,
        'hours': hours,
        'phone' : phone
    } 
    driver.get('https://google.com')
    return macroData

def run(checkboxInput, zip, price, type):
    data = {
        'checkboxInput': checkboxInput,
        'zip': zip,
        'price': price,
        'type': type
    }
    #bring up selenium & navigate to yelp page
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.yelp.com/search?find_desc=&find_loc=")
    putInFilters(data, driver)

    finalData = {}
    #pull data for each food type
    inputQuery(data, driver)
    restaurantTitles = compileResults(driver)
    #now that titles are stored in restaurantTitles, we search google and pull data.
    for title in restaurantTitles:
        searchRestaurant(title, data['zip'], driver)
        d = collectPageDataOnLoad(driver)
        finalData[title] = {
            'Rating':d['rating'],
            'Address':d['address'],
            'Hours':d['hours'],
            'Phone':d['phone']
            }
    driver.quit()
    f = open(r"C:\Users\charl\Documents\Professional\Coding\flsktst\data.json", 'w')
    f.write(json.dumps(finalData, indent=4, sort_keys=True))



'''
IDEAS:

--Use AI api to offer cheeky banter about food item while you wait
--Generate dictionary of dictionaries. Each entry is a resaurant, and you can use diff google location stats
to show star rating, customer reviews (make sexy w css)
--Revamp questions
--Use Streamlit to viusalize data
'''