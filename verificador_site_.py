import requests
import bs4
import re
from datetime import datetime, time, timedelta
from time import sleep

url_site = "https://instabio.cc/giovanafagundes"

TOKEN = '___'

interval = 3600
last_clock = time(hour=2, minute=58, second=0)

def sendMessage():
    global url_site

    url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        'chat_id' : ____,
        'text' : f'Atualização no Site: {url_site}'
    }
    requests.post(url_telegram,data=data)
    pass

def routine():

    headers = {
        "user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    req = requests.get(url_site, headers=headers)

    html = bs4.BeautifulSoup(req.content,'html.parser')

    def find_a_string(value):
        return lambda text: value in text
    
    web_element = html.find_all(string=find_a_string('21/09 -CURITIBA/PR (link em breve)'))

    mystring = ' '.join(map(str,web_element))

    f = mystring.find("21/09 -CURITIBA/PR (link em breve)")

    if f == -1:
        print("Pagina Atualizada")
        sendMessage()    

    print(f)
    print(mystring[f:(f+34)])


while True:
        routine()
        sleep(interval)
