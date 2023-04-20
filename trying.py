f=open("sample.txt","r")
i=f.readlines()
for j in i :
    j=j[0:4]
    print(j)
