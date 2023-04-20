import pickle
f=open("student.bin","rb+")
try:
    while True:
        m=pickle.load(f)
        print(m)
except EOFError:
    print("\n")
f.close()

#below is to be done in wb+ mode:
'''for i in  range(3):
    l=[]
    r=int(input("ENTER Roll no:"))
    n=input("ENTER name:")
    c=input("ENTER class:")
    l=[n,r,c]
    pickle.dump(l,f)
f.seek(0)
m=pickle.load(f)
print(m)
f.close()'''
