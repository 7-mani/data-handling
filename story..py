f=open("story.txt","w")
s=input("ENTER A STORY :")
a=s.split(".")
for i in a:
    f.write(i)
    f.write(".\n")
f.close()
