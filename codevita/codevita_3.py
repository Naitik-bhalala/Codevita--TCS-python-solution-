"""
enter number and find consicutive prime number's sum which is smaller than ypur entered number and sum should be prime number

ex:

     number : 20
          5(prime) = (2+3) prime
          17 (prime) = (2+3+5+7) prime


"""
num = int(input("enter number:"))
list1=list()
list3=list()
list2=list()
for ab in range(1,num):
    c=0
    for i in range(1,ab+1):
        if(ab%i==0):
            c=c+1
    if(c==2):
        list1.append(ab)
#print(list1)
su=0
e= list1[0]
d=len(list1)
count=0
for i in range(1,d):
    e = e +list1[i]
    f=0
    list2.append(e)
    for p in range(1,e+1):
        if(e%p==0):
            f=f+1
    if(f==2):
        if(e<num):
            #print(e)
            list3.append(e)
            count=count+1
#print("sum:",list2)
print("prime sum:",list3)
print(count)
    
    



            
