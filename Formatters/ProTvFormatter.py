import csv

with open("protv.csv", "r") as f:
    f.readline()
    l=[x.split(",") for x in f.readlines()]

for i in l:
    if(i[2].split(" ")[1]=='Ianuarie'):
        i[2]=i[2].split(" ")
        i[2][1]='01'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Februarie'):
        i[2]=i[2].split(" ")
        i[2][1]='02'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Martie'):
        i[2]=i[2].split(" ")
        i[2][1]='03'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Aprilie'):
        i[2]=i[2].split(" ")
        i[2][1]='04'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Mai'):
        i[2]=i[2].split(" ")
        i[2][1]='05'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Iunie'):
        i[2]=i[2].split(" ")
        i[2][1]='06'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Iulie'):
        i[2]=i[2].split(" ")
        i[2][1]='07'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='August'):
        i[2]=i[2].split(" ")
        i[2][1]='08'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Septembrie'):
        i[2]=i[2].split(" ")
        i[2][1]='09'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Octombrie'):
        i[2]=i[2].split(" ")
        i[2][1]='10'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Noiembrie'):
        i[2]=i[2].split(" ")
        i[2][1]='11'
        i[2]=".".join(i[2])
    elif(i[2].split(" ")[1]=='Decembrie'):
        i[2]=i[2].split(" ")
        i[2][1]='12'
        i[2]=".".join(i[2])

    i[3]=i[3].rstrip()

header = ["link_articol", "platforma", "data", "cuvinte_cheie"]

with open('protv.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(l)