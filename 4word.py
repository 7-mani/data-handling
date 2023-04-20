f=open("sample.txt","r")
a=f.readlines()
for k in range(len(a)):
    a[k]=a[k][0:4]
    print(a[k])
