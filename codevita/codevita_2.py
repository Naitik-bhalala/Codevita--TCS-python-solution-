"""
   write two number , among all the possible combination of fist number with exchanging two digit....find that number which should
    be a greater than second one and smallest among all posible solution.
  exa:
      
first number : 459
second number : 500

ans: 549

           

"""


inp = str(input("enter two number(seprated by space):"))
ttt = inp.split()

a = int(ttt[0])
b = int(ttt[1])
list1=list()
list5=list()
c=a

i=0


def Reverse(lst):
    lst.reverse()
    return lst

def convert(list):
    s = [str(n) for n in list]
    res = int("".join(s))
    return(res)

while(c>0):
    rem = int(c%10)
    c =int(c/10)  
    list1.append(rem) 



list2=Reverse(list1)
cou=len(list2)
p = cou-1
k=0
num = 0
for i in range(0,cou):
     for j in range(i+1,cou):
        list2[i],list2[j] = list2[j],list2[i]
        abc = convert(list2)
        if(abc>b):
            list5.append(abc)


        list2[i],list2[j] = list2[j],list2[i]
if(len(list5)==0):
    print("-1")
else:
    print(list5)
    print("min:",min(list5))
 
