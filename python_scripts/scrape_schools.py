import urllib.request, urllib.error, urllib.parse
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re


with open('schools.html', 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'lxml')

trList = list()

for tr in soup.findAll('tr'):
    if len(tr) <= 3: continue
    name = tr.findAll('td')[1].getText().replace(str('\n'),' ').strip()
    fullAddress = tr.findAll('td')[2].getText().replace(str('\n'),' ').strip()
    try:
        fullAddress = fullAddress.split('Эл.почта:')[0].split('Почтовый адрес:')[1].strip()
    except:
        fullAddress = ""

    try: 
        address = fullAddress.split(',')[0].strip()
    except:
        address = ""    

    try: 
        suburb = fullAddress.split(',')[1].strip()
    except:
        suburb = "" 
    
    try: 
        postcode = fullAddress.split(',')[3].strip()
    except:
        postcode = ""

    try:
        state = fullAddress.split(',')[2].strip().strip()
    except:
        state = ""

    try:
        nextToParse = fullAddress.split('Эл.почта:')[1]
    except:
        nextToParse = ""

    try:
        email = re.findall('(\S+@\S+)', tr.getText())[0]
    except:
        email = ""

    try:
        nextToParse = nextToParse.split('Веб-сайт:')[1]
    except:
         nextToParse = ""

    try:
        socialMedia = nextToParse.split('Фейсбук:')[1]
    except:
        socialMedia = ""

    try:
        website = re.findall('www.\S+', tr.getText())[0]
    except:
        website = ""

    person = tr.findAll('td')[3].getText().replace(str('\n'),' ').strip()
    details = tr.findAll('td')[4].getText().replace(str('\n'),' ').strip()
    hours = tr.findAll('td')[5].getText().replace(str('\n'),' ').strip()
    schools = {
        'name': name,
        'person': person,
        'email': email,
        'website': website,
        'social media': socialMedia,
        'address': address,
        'suburb': suburb,
        'postcode': postcode,
        'state': state,
        'details': details,
        'hours': hours,
        'full': tr.getText().replace(str('\n'),' ').strip()
    }
    trList.append(schools)
# print(trList)

with open('list.json', 'w', encoding='utf-8') as f:
    json.dump(trList, f, ensure_ascii=False, indent=4)



