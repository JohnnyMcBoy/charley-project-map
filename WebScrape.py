import requests
import pandas as pd
from bs4 import BeautifulSoup

# Get URL for data scraping
URL = "https://charleyproject.org/case-searches/advanced-search?first-name=&middle-name=&last-name=&suffix=&sex=&missing-since=&missing-from-city=&missing-from-state=&classification=&date-of-birth=&age=&height-and-weight=&distinguishing-chars=&clothing-jewelry-desc=&medical-conditions=&details-of-disappearance=&investigating-agency=&source-information="
#URL = "https://charleyproject.org/case-searches/alphabetical-cases?letter=U"       #Smaller Scale Test
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Gets all missing person cases in one list 
test=soup.find(id="case-container").find_all(class_="case")

# Creates lists to save variables to with the same size as the number of cases
size = len(test)
StoreLoc=[" "]*size
StoreName=[" "]*size
StoreMissFr=[" "]*size
StoreSex=[" "]*size
StoreRace=[" "]*size
StoreImg=[" "]*size

for i in range(0,size):
    #Get link of Caes
    test3=test[i].find('a').get('href')

    Tpage = requests.get(test3)

    Tsoup = BeautifulSoup(Tpage.content, "html.parser").find("article")

    # Scrape data
    Name = Tsoup.find(class_="title entry-title is-1").text
    Loc=Tsoup.find(id="case-top").find_all(class_="column")[1].find_all("li")[1].text.replace('Missing From', '').replace('\t', '').strip()
    MissFr=Tsoup.find(id="case-top").find_all(class_="column")[1].find_all("li")[0].text.replace('Missing Since', '').replace('\t', '').strip()
    Sex=Tsoup.find(id="case-top").find_all(class_="column")[1].find_all("li")[3].text.replace('Sex', '').replace('\t', '').strip()
    Race=Tsoup.find(id="case-top").find_all(class_="column")[1].find_all("li")[4].text.replace('Race', '').replace('\t', '').strip()

    Img=Tsoup.find(id="case-top").find_all(class_="column")[0].find_all("li")[0].find('img').get('src')

    #Store data
    StoreName[i]=Name
    StoreLoc[i]=Loc
    StoreMissFr[i]=MissFr
    StoreSex[i]=Sex
    StoreRace[i]=Race

    StoreImg[i]=Img

    #Show progress and save to csv every 100 cases
    if i%100==0:
        print(i)
        dict = {'Name':StoreName,'Location':StoreLoc,'Missing From':StoreMissFr,'Sex':StoreSex,'Race':StoreRace,'Image':StoreImg}
        df=pd.DataFrame(dict)
        df.to_csv('Test.csv')

#After loop finishes, save to csv one last time
dict = {'Name':StoreName,'Location':StoreLoc,'Missing From':StoreMissFr,'Sex':StoreSex,'Race':StoreRace,'Image':StoreImg}

df=pd.DataFrame(dict)

df.to_csv('Test.csv')
