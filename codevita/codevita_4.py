"""

 find the best bank between two

 both bank have differnt rate  for pertucular time slot.

 ex:
      input as    amount     :100000
                  total year : 20
                  number of slab(first bank): 3
                  period and rate (first bank):10 5.7     (period  & rate)
                                                5 6.9
                                                5 8.9


                  number of slab(second bank): 3
                  period and rate (second bank) 14 6.8
                                                4  6.9
                                                2  5.9


                  
      output     Bank A or Bank B
      

"""


p = int(input("amount:"))
n = int(input("total years:"))


def emi(p,r):
    sq = pow((1 + r),(p*12))
    emi = float(p * r / (1-1/(sq)))
    return emi
s1 = int(input("number of slab:"))
print("period and rate for first bank(sep by space):")
total1 = 0
for i in range(s1):
    pr1 = str(input())
    l1= pr1.split(" ")
    p1 = int(l1[0])
    r1 = float(l1[1])
    first1 = emi(p1,r1)
    #print(first)
    total1 = total1 + first1

#print(total1)
s2 = int(input("number of slab:"))
print("period and rate for second bank(sep by space):")
total2 = 0
for i in range(s2):
    pr2 = str(input())
    l2= pr2.split(" ")
    p2 = int(l2[0])
    r2 = float(l2[1])
    first2 = emi(p2,r2)
    #print(first)
    total2 = total2 + first2

#print(total2)

if(total1>total2):
    print("Bank B")
else:
    print("Bank A")




