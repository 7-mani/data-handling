f=open("sample.txt","r")
a=f.readlines()
for i in a:
    print(i[-2])
