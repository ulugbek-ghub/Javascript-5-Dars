
from googletrans import Translator

tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)

matn_uz = "Adhambek eng rasvo o'quvchim bundan rasvo odam yo'q"

tarjima = tarjimon.translate(matn_uz)

print(tarjima.text)
##Orginal matn
print(tarjima.origin)
## Orginal matn tili
print(tarjima.src)
##
#### Rus tiliga tarjima
##tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
##print(tarjima_ru.text)

# Ingiliz tilidan o'zbek tiliga tarjima
##matn_en = "Tashkent is the capital of Uzbekistan"
##tarjima_uz = tarjimon.translate(matn_en, dest='uz')
##print(tarjima_uz.text)


## requests API
## pip install requests

import requests
from pprint import pprint

##manzil= "https://kun.uz/news/main"
##r = requests.get(manzil)
##pprint(r.text)


##url = f"https://jsonplaceholder.typicode.com/todos"
##r = requests.get(url)
##r_json = r.json()
##print(r_json)

##import requests
##import googletrans
##
##url = "https://api.adviceslip.com/advice"
##r = requests.get(url)
##advice = r.json()['slip']['advice']
##
##print(advice)
##
##translator = googletrans.Translator()
##tarjima = translator.translate(advice, dest='uz')
##print(tarjima.text)


##import requests
##from bs4 import BeautifulSoup
##
##sahifa = "https://kun.uz/news/main"
##r = requests.get(sahifa)
##
##
##soup = BeautifulSoup(r.text, 'html.parser')
##news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
####print(news[2].text) # eng birinchi yangilikni konsolga chiqaramiz
##
