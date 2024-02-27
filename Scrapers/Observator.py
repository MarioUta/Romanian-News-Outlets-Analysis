import csv
import requests
from bs4 import BeautifulSoup

with open("badwords.txt","r") as f:
    badwords=f.readlines()
    badwords=[x.rstrip() for x in badwords if x[0]!= "#"]
    

header = ["link_articol", "platforma", "data", "cuvinte_cheie"]
with open('observator.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
        
    for c in range(1,268):

        markup = requests.get(f'https://observatornews.ro/politic/?p={c}').text
        soup=BeautifulSoup(markup,'html.parser')
        links=soup.findAll("div", {"class": "stire"})

        for link in links:
        
            l=link.a.get('href')
            text=link.a.text.lower()
            cuvinte_cheie=[]
            data=link.find("span", {"class": "data-publicare"}).text.split(" ")[1]

            for cuv in badwords:
                if cuv in text:
                    cuvinte_cheie.append(cuv)
            cuvinte_cheie=" ".join(cuvinte_cheie)

            if("la" not in data):
                if(len(cuvinte_cheie)):
                    writer.writerow([l, ' observator',data,cuvinte_cheie])
                else:
                    writer.writerow([l, ' observator',data,'nothing'])

    for c in range(1,215):

            markup = requests.get(f'https://observatornews.ro/economic/?p={c}').text
            soup=BeautifulSoup(markup,'html.parser')
            links=soup.findAll("div", {"class": "stire"})

            for link in links:
            
                l=link.a.get('href')
                text=link.a.text.lower()
                cuvinte_cheie=[]
                data=link.find("span", {"class": "data-publicare"}).text.split(" ")[1]

                for cuv in badwords:
                    if cuv in text:
                        cuvinte_cheie.append(cuv)
                cuvinte_cheie=" ".join(cuvinte_cheie)

                if("la" not in data):
                    if(len(cuvinte_cheie)):
                        writer.writerow([l, ' observator',data,cuvinte_cheie])
                    else:
                        writer.writerow([l, ' observator',data,'nothing'])

    for c in range(1,1653):

            markup = requests.get(f'https://observatornews.ro/extern/?p={c}').text
            soup=BeautifulSoup(markup,'html.parser')
            links=soup.findAll("div", {"class": "stire"})

            for link in links:
            
                l=link.a.get('href')
                text=link.a.text.lower()
                cuvinte_cheie=[]
                data=link.find("span", {"class": "data-publicare"}).text.split(" ")[1]

                for cuv in badwords:
                    if cuv in text:
                        cuvinte_cheie.append(cuv)
                cuvinte_cheie=" ".join(cuvinte_cheie)

                if("la" not in data):
                    if(len(cuvinte_cheie)):
                        writer.writerow([l, ' observator',data,cuvinte_cheie])
                    else:
                        writer.writerow([l, ' observator',data,'nothing'])

