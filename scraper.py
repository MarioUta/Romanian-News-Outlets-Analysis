import csv
import requests
from bs4 import BeautifulSoup

with open("badwords.txt","r") as f:
    badwords=f.readlines()
    badwords=[x.rstrip() for x in badwords if x[0]!= "#"]
    

header = ["link_articol", "platforma", "data", "cuvinte_cheie"]
with open('digi24.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for c in range(1, 100):
        markup = requests.get(f'https://www.digi24.ro/ultimele-stiri?p={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("article", {"class": "article brdr"})
        
        for i in links:
            link= "https://www.digi24.ro"+i.a.get('href')
            text=i.a.text.lower()
            date=i.time.text
            cuvinte_cheie=[]
            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)
            if(len(cuvinte_cheie)):
                writer.writerow([link, ' digi24',date,cuvinte_cheie])
            else:
                writer.writerow([link, ' digi24',date,'nothing'])

    
