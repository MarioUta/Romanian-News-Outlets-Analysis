import csv

with open("digi24.csv", "r") as f:
    f.readline()
    l=[x.split(",") for x in f.readlines()]


for i in l:
    i[2]=i[2].split(" ")[1]
    i[3]=i[3].rstrip()

header = ["link_articol", "platforma", "data", "cuvinte_cheie"]

with open('digi24.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(l)