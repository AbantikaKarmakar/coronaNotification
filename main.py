from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r'C:\Users\Lenovo\Desktop\Virtual Environment\CoronaNotification\corona.ico',
        timeout = 6
    )
    
def getData(url):
    r = requests.get(url)
    return r.text
    
if __name__ == "__main__":
    while True:
        # notifyMe("Amaya", "Lets stop the spread of this virus together.")
        myHtmlData  = getData('https://www.mohfw.gov.in/')
        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.getText()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        
        states = ['Chandigarh', 'Telangana', 'Utter Pradesh']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]} Indian : {dataList[2]}\nForeign : {dataList[3]} Cured : {dataList[4]}\nDeaths : {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
                
        time.sleep(3600)