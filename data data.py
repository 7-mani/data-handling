f=open("data.txt","w")
l,d=[],{}
n=int(input("number of students :"))
for i in range(n):
    r=input("ENTER ROLL NUMBER :")
    na=input("ENTER NAME :")
    s=input("ENTER SUBJECTS YOU HAVE CHOOSEN:")
    m=d[r]=[na,s]
    l.append(m)
f.writelines(l)
f.close()

    
