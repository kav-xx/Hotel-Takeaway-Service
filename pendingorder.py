from pickle import load,dump


#A function which reads in file and read into a list of list
def file_order(d):
    f=open('order.txt','r')
    r=f.readlines()
    l=[]
    for i in r:
        j=i.split(',')
        l1=j[-1]
        l2=d[str(int(l1))]
        l.append([l1,l2])
    f.close()
    return l


#Allows the manager to update the pending orders
def choice(l):
    while True:
        print('''Choice
                 1.Display
                 2.Delete
                 3.Exit''')
        ch=int(input('Enter the choice'))
        if ch==1:
            if l==[]:
                print('No pending orders')
                continue
            for i in l:
                print('Order No.=',i[0],'Items=',i[1])
                
        elif ch==2:
            if l==[]:
                print('No pending orders')
                continue
            order=input('Enter the OrderNo. which is to be deleted')
            lst=[str(int(j[0])) for j in l]
            if order not in lst:
                print('Improper order No.')
                continue
            for i in l:
                if str(int(i[0]))==order:
                    temp=i
                    break
            ind=l.index(i)
            
            a=l.pop(ind)
            f1=open('bill.bin','ab+')
            f2=open('order.txt','a+')
            f2.seek(0,0)
            read=f2.readlines()
            req=[]
            for i in read:
                b=i.split(',')
                if int(b[-1])==int(a[0]):
                    pass
                else:
                    req.append(i)
            f1.seek(0,0)
            f2.seek(0,0)
            f2.truncate()
            f1.truncate()
            f2.writelines(req)
            dump(dict(l),f1)
            f1.close()
            f2.close()
        elif ch==3:
            exit()
        else:
            print('Invalid Choice')

def delete_items(order_no):
    
    file=open('bill.bin','rb')
    data=load(file)
    # keys=list(data.keys())
    # values=list(data.values())
    # for i in range(len(keys)):
    #     keys[i]=str(int(keys[i]))
    # data=dict(zip(keys,values))
    require=data[str(order_no)]
    maintain=[]
    for i in data:
        a=[i,data[i]]
        maintain.append(a)
    with open('bill.bin','ab+') as file:
        file.seek(0,0)
        d=load(file)
        d.pop(str(order_no))
        file.seek(0,0)
        file.truncate()
        dump(d,file)
    with open('order.txt','a+') as file:
        file.seek(0,0)
        read=file.readlines()
        final=[]
        for i in read:
            a=i.split(',')
            if int(a[-1])==int(order_no):
                pass
            else:
                final.append(i)
        file.seek(0,0)
        file.truncate()
        file.writelines(final)
#Driver code 
# file=open('bill.bin','rb')
# data=load(file)
# print(data)
# result=file_order(data)
# choice(result)
        
            
            
