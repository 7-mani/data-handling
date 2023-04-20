#s=input("ENTER A STRING:")
f=open("list of practicles.txt",'r')
l=f.readlines()
for i in l:
    k=i.split()
    for j in k:
        if k[-1]=="\n":
            print("\n",end='\n')
        else:
            print(j+'#',end="")
    
