#Importing necessary modules
from datetime import datetime
import os
from pickle import load,dump


#To find whether teh preference to be given to the order or not
def timediff(a,b):
    c = datetime.strptime(a, "%H:%M:%S")
    d = datetime.strptime(b, "%H:%M:%S")
    difference = c - d
    seconds = difference.total_seconds()    
    minutes = seconds / 60
    if minutes <2:
        return True
    return False


#To check whether teh file is empty or not
def fileisempty(filename):
    if os.path.getsize(filename) == 0:
        return True
    return False


#Load contents into file
def file(file_name):
    file=open(file_name+'.txt','rb')
    while True:
        try:
            d=load(file)
            if file_name.name in d:
                return d[file_name.name]
        except:
            return []

def check(data,l):
    c = int(l[3])
    d = int(data[3])
    minutes = c - d
    if minutes>=5:
        return True
    return False

# Queue data structure for organising the orders as per priority
class AdapterPriorityQueue:
    
    
    def __init__(self):
        if fileisempty('order.txt'): 
            self.item=[]
            self._order=0
        else:
            l=[]
            f=open('order.txt','r')
            f.seek(0)
            r=f.readlines()
            for i in r:
                l.append(i)
            f.close()
            self.item=l
            self._order=len(r)
            
            
    def enqueue(self,value):#['00:00:00',quant,no,total_time]
        self._order+=1
        if self.item!=[]:
            s=self.item[-1]
            l=s.split(',')
            data=value.split(',')
            if int(data[1])<3 and check(data,l) and int(l[1])>3:
                if timediff(data[0],l[0]):
                    ind=self.item.index(s)
                    self.item.insert(ind,value+','+str(self._order)+'\n')
                else:
                    self.item.append(value+','+str(self._order)+'\n')
            else:
                self.item.append(value+','+str(self._order)+'\n')
        else:
            self.item.append(value+','+str(self._order)+'\n')
        return self._order

    
    
    def dequeue(self):
        if self.item!=[]:
            self.item.pop(0)
            self._order-=1
            return self._order
        else:
            raise 'Queue is Empty'
        
    def addintofile(self):
        f=open('order.txt','w')
        for i in self.item:
            f.write(i)
        f.close()


 #Addition of order       
def addorder(data):
    aq=AdapterPriorityQueue()
    result=aq.enqueue(data)
    aq.addintofile()
    return result



#Deletion of order    
def delorder():
    aq=AdapterPriorityQueue()
    result=aq.dequeue()
    aq.addintofile()
    return result

 
#Upadate the orders   
def update(l):
    now_time=datetime.now()
    if now_time.hour in range(0,12):
        f1=open('breakfast.txt','a+')            
    elif now_time.hour in range(12,18):
        f1=open('lunch.txt','a+') 
    elif now_time.hour in range(18,24):
        f1=open('dinner.txt','a+') 
        
    f2=open('chat.txt','a+')
    f1.seek(0)
    f2.seek(0)
    r1=f1.readlines()
    r2=f2.readlines()
    for i in range(len(r1)):
        s1=r1[i].split(',')
        if int(s1[-2])>0:
            z1=list((zip(*l)))
            if s1[1] in z1[0]:
                ind=list(z1[0]).index(s1[1])
                s1[2]=str(int(s1[2])-int(l[ind][1]))
                r1[i]=','.join(s1)
    for i in range(len(r2)):
        s2=r2[i].split(',')
        if int(s2[-2])>0:
            z2=list((zip(*l)))
            if s2[1] in z2[0]:
                ind=list(z2[0]).index(s2[1])
                s2[2]=str(int(s2[2])-int(l[ind][1]))
                r2[i]=','.join(s2) 
    f2.seek(0)   
    f1.seek(0)
    f1.truncate()
    f2.truncate()
    f1.writelines(r1)
    f2.writelines(r2)
    f1.close()
    


def order_list(time=None):
    result={}
    if time is not None:
        if time in range(0,12):
            file=open('breakfast.txt')            
        elif time in range(12,18):
            file=open('lunch.txt')
        elif time in range(18,24):
            file=open('dinner.txt')
    else:
        file=open('chat.txt')
    list1=file.readlines()
    for i in list1:
        s=i[:-1].split(',')
        result[s[1]]=[s[2],s[3]]
    file.close()
    return result,file.name[:-4]
##addorder('4:25:50,3,1')
        
