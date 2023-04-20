f=open("sample.txt","r")
a=f.readlines()
for i in a:
    k=i.split()
    for j in k:
        print(j[-1],end=" ")
