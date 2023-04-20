f=open("sample.txt","r")
max,s=0,""
for i in range(6):
    k=f.readline()
    if max<len(k):
        s=k
print("largest ",k)
        
