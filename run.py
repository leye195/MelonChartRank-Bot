
import re
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from settings import getWebHooks
from slack import WebhookClient

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome("chromedriver",options=options)
driver.implicitly_wait(3)

def send_slack(blocks):
    payload,url={"blocks":blocks[:21]},getWebHooks()
    #print(url)
    requests.post(url=url,data=json.dumps(payload),headers={"Content-Type":"application-json"})
    #slack.chat_postMessage(channel=channel_name,blocks=blocks[:21])
def extract_rank(type=0):
    url,date,title="","",""
    if(type==0):
        url = "https://www.melon.com/chart/index.htm"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    #real_conts > div.multi_row > div.calendar_prid > span.yyyymmdd > span
    if(type==0):
        date = soup.select_one("#conts > div.multi_row > div.calendar_prid.mt12 > span.yyyymmdd").get_text().strip()
        title = f"{date} 실시간 음원 순위 알림"
    '''elif(type==1):
        date = soup.select_one("#conts > div.calendar_prid > span.yyyymmdd > span").get_text().strip()
        title = f"{date} 일간 음원 순위 알림"
    else:
        date = soup.select_one("#conts > div.calendar_prid > span").get_text().strip()  
        if(type==2):
            title= f"{date} 주간 음원 순위 알림"
        elif(type==3):
            title = f"{date} 월간 음원 순위 알림"'''
    blocks,block=[],dict()
    chart = soup.select("#frm > div > table > tbody > tr")
    blocks.append({
            "type": "section",
			"text":{
                "type":"mrkdwn",
                "text":f"*{title}*"
            },
            "block_id": "text1"
    })
    idx = 0
    for c in chart:
        rank = idx+1
        image_url = c.select_one("td:nth-child(2) > div > a > img")["src"]
        title = c.select_one("td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a").get_text().strip()
        singer = c.select_one("td:nth-child(4) > div > div > div.ellipsis.rank02 > a").get_text().strip()
        album_info = c.select_one("td:nth-child(5) > div > div > div > a")
        album_title,album_link = album_info.get_text().strip(),f"https://www.melon.com/album/detail.htm?albumId={re.search('[0-9]+',album_info['href']).group()}"
        like = c.select_one("td:nth-child(6) > div > button > span.cnt").get_text().strip("")[5:]
        block={
           "type":"section",
           "text":{
               "type":"mrkdwn",
               "text":f"{rank} {title}\n<{album_link}|{singer} | {album_title}>\n💖{like}개"
           },
           "accessory":{
               "type":"image",
               "image_url":image_url,
               "alt_text":title
           }
        }
        blocks.append(block)
        idx+=1
    send_slack(blocks)
    driver.quit()

def main():
    extract_rank()

if __name__== '__main__':
    main()
