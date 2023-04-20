import pickle

f=open("binary.bin","wb")
d={1:"sonu",2:"mani"}
pickle.dump(d,f)
f.close()
