f=open("hello.txt","r")
s=f.read()
p=s.split()
m=0
for i in p:
    if len(i)> m:
        m=len(i)
        k=i
print("largest letter in a file :",k,"\nlength of letter :",m)
    
