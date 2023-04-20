import pickle
def create():
    f=open("bin11.bin","wb")
    while True:
        k=eval(input("Enter student data: roll.no,name,marks..as a list"))
        pickle.dump(k,f)
        a=input("do u want to continue??....Y/N")
        if a=="n":
            break
    f.close()
    
def display():
    f=open("bin11.bin","rb")
    try:
        while True:
            a=pickle.load(f)
            print(a)
    except:
        print("THANK YOU!!!")
    f.close()

def search():
    f=open("bin11.bin","rb")
    a=int(input("Enter roll.no that you want to update for:"))
    try:
        while True:
            l=pickle.load(f)
            if l[0]== a :
                print("Record found:",l)
                break  
    except:
        print("Record not found try again")
    f.close()

# let user fix marks limit, counting the no.of records are there of those marks limit
def count():
    f=open("bin11.bin","rb")
    c=0
    k=int(input("Enter marks limit :"))
    try:
        while True:
            s=pickle.load(f)
            if s[2]>=k:
                c+=1
                print(s)
    except:
        print("no of records that are above the range",k,"are :",c)
    f.close()
    
#updating .bin files "rb+"access mode, updating name of a record
def update():
    f=open("bin11.bin","rb+")
    r=int(input("enter roll number to be updated :"))
    n=input("Enter updated marks :")
    try :
        while True:
            ps=f.tell()
            print(ps)
            a=pickle.load(f)
            if a[0]==r:#r=2
                a[2]= n
                break
        f.seek(ps)
        pickle.dump(a,f)            
    except:
        print("\n")
    f.close()
create()
display()
search()





















    
