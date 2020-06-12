"""
number of sample and number of range  :  5 2
    (then enter sample)

      12 23 34 45 56

    (then enter first range )

       23 45


    (then enter second range )

       46 60

output : 
      1 1

      here fisrt ans from the number of sample which is in first range
       here second ans from the number of sample which is in second range




"""



it = str(input("no of sample and range:"))
list1 = list()
list2 = list()
ab= it.split(" ")
sam = int(ab[0])
ran = int(ab[1])
bc = str(input())
data = bc.split(' ')
#print(data[0:10])

for i in range(ran):
    c=0
    rc = str(input())
    rang =rc.split(" ")
    #print(rang)
    for j in range(sam):
        if(int(data[j])>int(rang[0]) and int(data[j])<int(rang[1])):
            #print(data[j])
            c = c+1
    list2.append(c)

for k in range(ran):
    print(list2[k],end=" ")


