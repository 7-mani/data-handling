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
