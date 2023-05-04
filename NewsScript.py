from bs4 import BeautifulSoup as bs
import requests
import pyttsx3 as tts
import subprocess
engine=tts.init()
engine.setProperty('voice','English (America, New York City)')
engine.setProperty('rate',150)

response = requests.get('https://www.opindia.com/latest-news/')

soup = bs(response.content,'html.parser')

a = soup.select('a[rel="bookmark"]')
news=[]

for i in range(10):
        title = str(a[i].get('title'))
        if ( title != '')  and (title not in news):
            news.append(a[i].get('title'))

for title in news:
        subprocess.run(['notify-send','News','-t','0',title])
        engine.say(title)
        engine.runAndWait()
