from bs4 import BeautifulSoup as bs
import requests
import os
os.mkdir('Wallpapers')

response = requests.get('https://wallhaven.cc/latest')

soup = bs(response.content,'html.parser')

links = soup.select('a.preview')

for i in range(10):
    link = links[i].get('href')
    response = requests.get(str(link))
    soup = bs(response.content,'html.parser')
    imageSrc = soup.find_all(id='wallpaper')[0].get('src')
    
    response = requests.get(str(imageSrc))
    with open(f'./Wallpapers/{i}.jpg','wb') as file:
        file.write(response.content)