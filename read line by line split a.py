import csv
f=open("list of practicles.txt","r")
k=f.readlines()
for i in k:
    q=i.split('a')
    for j in q:
        print(j)


