#create employee data base with empcode , name and salary
# search a employee by empcode and update the salary of employee
#add new employee to the file ,count no of employees with more than 2000 salary.
import pickle
def addrec():
    f=open("employee.bin","ab+")
    l=[]
    e=int(input("Enter empcode:"))
    n=input("Enter employee name :")
    sl=int(input("Enter salary of employee :"))
    l=[e,n,sl]
    pickle.dump(l,f)
    f.close()

def display():
    f=open("employee.bin","rb")
    try :
        while True:
            l=pickle.load(f)
            print(l)
    except:
        print("Thank you!!")
    f.close()

def search(empcode):
    f=open("employee.bin","rb")
    try :
        while True:
            l=pickle.load(f)
            if l[0]== empcode :
                print("Employee record found",l)
                return 1
                break
    except:
        print("Employee record not found")
        return 0
    f.close()
                
def update():
    f=open("employee.bin","r+b")
    e=int(input("Empcode of employee of salary updation :"))
    a=search(e)
    if a==1:
        n=int(input("Enter salary to be updated :"))
        try:
            while True:
                ps=f.tell()
                l=pickle.load(f)
                if l[0]==e:
                    l[2]=n
                    break
            f.seek(ps)
            pickle.dump(l,f)
        except:
            return 0
    else:
        print("\n   Employee Record not found\n\n")
    f.close()
    
def count():
    f=open("employee.bin","rb")
    c=0
    k=int(input("enter salary limit :"))
    try :
        print("records are :")
        while True:
            s=pickle.load(f)
            if s[2]>=k:
                c+=1
                print(s)
    except:
        print("no of records =",c)
    f.close()

#main program
while True:
    print("\n1.Add new record 2.Display 3.Search 4.Update salary  5.Count no.of employees >/< the range 6.exit")
    n=int(input("Enter choice :"))
    if n==1:
        addrec()
    elif n==2:
        display()
    elif n==3:
        k=int(input("Enter empcode"))
        search(k)
    elif n==4:
        update()
    elif n==5:
        count()
    else:
        print("\n\nThank you!!")
        break
        


