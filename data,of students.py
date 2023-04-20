f=open("data.txt","w")
o,sub="",""
k=int(input("ENTER NUMBER OF STUDENTS :"))
for i in range(k):
    a=input("ENTER NAME :")
    r=input("ENTER ROLL NUMBER :")
    o=a+",",r+","
    for i in range(6):
        sub=input("ENTER YOUR SUBJECTS:")
        print(type(sub))
        sub=sub+","
        o=o+sub
    f.write(o+"\n")
f.close()

       
