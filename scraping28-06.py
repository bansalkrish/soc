from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

chrome_options = Options()
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

stockdata = {"Symbol":[], "Open":[],"High":[], "Low":[],"Prev.Close":[], "LTP":[], "CHNG":[], "%CHNG":[],"Volume":[]}

symbolarray = []
openarray =[]
higharray=[]
lowarray=[]

driver.get("https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050")
driver.maximize_window()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))
# data = []
table = driver.find_element(By.ID, "equityStockTable")
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    try:
        tds = row.find_elements(By.TAG_NAME, "td")
        
        symbolarray.append(tds[0].text)
        openarray.append(tds[1].text)
        higharray.append(tds[2].text)
        lowarray.append(tds[3].text)
        stockdata["Prev.Close"].append(tds[4].text)
        stockdata["LTP"].append(tds[5].text)
        stockdata["CHNG"].append(tds[6].text)
        stockdata["%CHNG"].append(tds[7].text)
        stockdata["Volume"].append(tds[8].text)
     
    except Exception as e:
        continue

for i in range(0,51):
    stockdata["Symbol"].append(symbolarray[2*i])    # I am doing this beacause for these 4 sections,
    stockdata["Open"].append(openarray[2*i])        # I was getting 1 extra entry of a blank space
    stockdata["High"].append(higharray[2*i])        # after every significant entry. 
    stockdata["Low"].append(lowarray[2*i])          # So I took every alternate entry into the main csv file.

    # cells = row.find_element(By.TAG_NAME , "td")
    # row_data = []
    # for cell in cells:
    #     row_data.append(cell.text)
    # data.append(row_data)
    # for i in range(0,51):
print(stockdata["Symbol"])
print(stockdata["Open"])
print(stockdata["High"])
print(stockdata["Low"])
print(stockdata["Prev.Close"])
print(stockdata["LTP"])
print(stockdata["CHNG"])
print(stockdata["%CHNG"])
print(stockdata["Volume"])

      
print(len(stockdata["Symbol"]))
print(len(stockdata["Open"]))
print(len(stockdata["High"]))
print(len(stockdata["Low"]))
print(len(stockdata["Prev.Close"]))
print(len(stockdata["LTP"]))
print(len(stockdata["CHNG"]))
print(len(stockdata["%CHNG"]))
print(len(stockdata["Volume"]))
time.sleep(5)
driver.quit()    
df = pd.DataFrame.from_dict(stockdata)
df.to_csv("stockdata.csv", index = False)
df

