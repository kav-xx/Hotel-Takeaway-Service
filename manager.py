#This functions allows the manager to add items into the file
def additem(file,list1):
    f=open(file+'.txt','a+')
    f.seek(0)
    r=f.readlines()
        
    last=r[-1]
    l=last.split(',')
    l1=l[0][0]
    l2=str(1+int(l[0][1]))
    code=l1+l2
    st='{},{},{},{},{}'.format(code,list1[0],list1[1],list1[2],list1[3])+'\n'
    f.seek(2)
    f.write(st)
    f.close()
    
        
#This function enables to delete items from the file
def delitem(file,delcode):
##        print('''Options
##                 1.Delete for Breakfast
##                 2.Delete for Lunch
##                 3.Delete for Dinner
##                 4.Delete for Snacks
##                 5.Go Back''')
##        ch=int(input('Enter the choice'))
##        if ch==5:
##            break
##        elif ch==1:
##            f=open('breakfast.txt','a+')
##        elif ch==2:
##            f=open('lunch.txt','a+')
##        elif ch==3:
##            f=open('dinner.txt','a+')
##        elif ch==4:
##            f=open('chat.txt','a+')
##        elif ch not in [1,2,3,4,5]:
##            print('Give Valid Choice')
##            continue
##        delcode=input('Enter the code of the item to be deleted')
    f=open(file+'.txt','a+')
    f.seek(0)
    r=f.readlines()
    print(r)
    for i in range(len(r)):
        print(r[i][0]+r[i][1],delcode)
        if r[i][0]+r[i][1]==delcode:
            r.pop(i)
            f.seek(0)
            f.truncate()
            f.writelines(r)
            f.close()
            break

#It allows the manager to update availability,price,items,etc
def updateitem(file,data):
    # while True:
    #     print('''Options
    #              1.Update for Breakfast
    #              2.Update for Lunch
    #              3.Update for Dinner
    #              4.Update for Snacks
    #              5.Go Back''')
    #     ch=int(input('Enter the choice: '))
    #     if ch==5:
    #         break
    #     elif ch not in [1,2,3,4,5]:
    #         print('Enter valid choice: ')
    #         continue
    #     elif ch==1:
    #         f=open('breakfast.txt','a+')
    #     elif ch==2:
    #         f=open('lunch.txt','a+')
    #     elif ch==3:
    #         f=open('dinner.txt','a+')
    #     elif ch==4:
        f=open(file+'.txt','a+')
        f.seek(0)
        read=f.readlines()
        l=[]
        for i in read:
            a=i.split(',')
            if a[0]==data[0]:                
                l.append(','.join(data)+'\n')
            else:
                l.append(i)
        f.seek(0)
        f.truncate()
        f.writelines(l)
        f.close()
        # if icode in f.read():
        #     while True:
        #         print('''Options
        #                  1.Update quantity availability
        #                  2.Upadate price
        #                  3.Exit''')
        #         ch=int(input('Enter the choice: '))
        #         if ch==3:
        #             break
        #         elif ch not in [1,2,3]:
        #             print('Invalid Choice')
        #             continue
        #         elif ch==1:
        #             index=2
        #             up=input('Enter the updated quantity availability: ')
        #         elif ch==2:
        #             index=3
        #             up=input('Enter the updated price: ')
        #         f.seek(0)
        #         r=f.readlines()
        #         for i in range(len(r)):
        #             temp=r[i]
        #             s=temp.split(',')
        #             print(s)
                    
                    
        #             if s[0]==icode:
        #                 s[index]=up
        #                 r[i]=','.join(s)+'\n'
        #                 print(r)
        #                 f.seek(0)
        #                 f.truncate()
        #                 f.writelines(r)
        #                 break
        #         f.close()
        # else:
        #     print('Item not found')
        
                             
 #Allows the manager to update menu               
def UpdateMenu():
    while True:
        print('''Options
                 1.Add new item
                 2.Delete item
                 3.Update item
                 4.Go Back''')
        ch=int(input('Enter the choice: '))
        if ch==1:
            additem()
        elif ch==2:
            delitem()
        elif ch==3:
            updateitem()
        elif ch==4:
            break
        else:
            print('Give proper choice....')
            
            
#Displays menu to the manager
def display():  
    while True:
        print('''Options
                 1.Display for Breakfast
                 2.Display for Lunch
                 3.Display for Dinner
                 4.Display for Snacks
                 5.Go Back''')
        ch=int(input('Enter the choice: '))
        if ch not in [1,2,3,4,5]:
            print('Enter the Valid choice: ')
            continue
        if ch==5:
            break
        elif ch==1:
            file=open('breakfast.txt')
        elif ch==2:
            file=open('lunch.txt')
        elif ch==3:
            file=open('dinner.txt')
        elif ch==4:
            file=open('chat.txt')
        list1=file.readlines()
        print('Code\tFood item\tQuantity\tCost')
        for i in list1:
            a=i.split(',')
            for j in a:
                print(j,end='\t')
            print()     
            
                  
#A function which allows various operations for the manager
def Manager():
    while True:
        print('''Options
                 1.Display Menu
                 2.Update Menu
                 3.Exit''')
        ch=int(input('Enter the choice: '))
        if ch==1:
            display()
        elif ch==2:
            UpdateMenu()
        elif ch==3:
            break
        else:
            print('Give proper choice...')

