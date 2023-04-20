f=open("sample.txt","r+")
k=f.read()
f.write("HI read and write access mode will append at last")
f.write("all gone mad!!!!")
print(k)
f.close()



