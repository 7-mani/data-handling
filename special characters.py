f=open("sample.txt","r")
s,c=f.read(),0
l="!@#$%^&*()_+~` -=+_[]{}':;|\><,./?"
for i in s:
    if i in l :
        c+=1
print("number of special charaters :",c)
