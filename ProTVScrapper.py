import csv
import requests
from bs4 import BeautifulSoup

with open("badwords.txt","r") as f:
    badwords=f.readlines()
    badwords=[x.rstrip() for x in badwords if x[0]!= "#"]
    

header = ["link_articol", "platforma", "data", "cuvinte_cheie"]
with open('protv.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    for c in range(1,510):
        markup = requests.get(f'https://stirileprotv.ro/stiri/politic/?page={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("div", {"class": "article-title"})
        dates=soup.findAll("div", {"class": "article-date"})


        for link,date in zip(links,dates):
        
            l=link.h2.a.get('href')
            text=link.h2.a.text.lower()
            data=" ".join(date.text.split(' ')[1:]).rstrip()

            cuvinte_cheie=[]
            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)
    
            if("ora" not in data and "minut" not in data):
                if(len(cuvinte_cheie)):
                    writer.writerow([l, ' protv',data,cuvinte_cheie])
                else:
                    writer.writerow([l, ' protv',data,'nothing'])

    for c in range(1,412):
        markup = requests.get(f'https://stirileprotv.ro/stiri/financiar/?page={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("div", {"class": "article-title"})
        dates=soup.findAll("div", {"class": "article-date"})
        for link,date in zip(links,dates):
        
            l=link.h2.a.get('href')
            text=link.h2.a.text.lower()
            data=" ".join(date.text.split(' ')[1:]).rstrip()
            cuvinte_cheie=[]
            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)
            if("ora" not in data and "minut" not in data):
                if(len(cuvinte_cheie)):
                    writer.writerow([l, ' protv',data,cuvinte_cheie])
                else:
                    writer.writerow([l, ' protv',data,'nothing'])

    for c in range(1,624):
        markup = requests.get(f'https://stirileprotv.ro/stiri/social/?page={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("div", {"class": "article-title"})
        dates=soup.findAll("div", {"class": "article-date"})
        for link,date in zip(links,dates):
                
            l=link.h2.a.get('href')
            text=link.h2.a.text.lower()
            data=" ".join(date.text.split(' ')[1:]).rstrip()
            cuvinte_cheie=[]
            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)
            if("ora" not in data and "minut" not in data):
                if(len(cuvinte_cheie)):
                    writer.writerow([l, ' protv',data,cuvinte_cheie])
                else:
                    writer.writerow([l, ' protv',data,'nothing'])
        
    for c in range(1,2079):
        markup = requests.get(f'https://stirileprotv.ro/stiri/international/?page={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("div", {"class": "article-title"})
        dates=soup.findAll("div", {"class": "article-date"})
        for link,date in zip(links,dates):
        
            l=link.h2.a.get('href')
            text=link.h2.a.text.lower()
            data=" ".join(date.text.split(' ')[1:]).rstrip()
            cuvinte_cheie=[]
            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)
            if("ora" not in data and "minut" not in data):
                if(len(cuvinte_cheie)):
                    writer.writerow([l, ' protv',data,cuvinte_cheie])
                else:
                    writer.writerow([l, ' protv',data,'nothing'])
        
    
