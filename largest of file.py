f=open("sample.txt","r")
max,a,s=0,f.readlines(),""
for i in range(len(a)):
    if max<len(a[i]):
        max,s = len(a[i]),a[i]
print("largest line of file :",s)
