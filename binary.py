from pickle import load,dump

file=open('bill.bin','rb')
a=load(file)
file.close()
keys=list(a.keys())
value=list(a.values())
for i in range(len(keys)):
    keys[i]=str(int(keys[i]))
file=open('bill.bin','wb')
dump(dict(zip(keys,value)),file)
file.close()