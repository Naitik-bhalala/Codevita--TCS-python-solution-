# find min number of coins required to form any value betwwen 1 to n
#coins are 5,2,1 rupees


coin = int(input("number of coin:"))
list=[ [0,0,0] ,
[0,0,1],
[0,0,2],
[0,1,1],
[0,1,2],
[0,2,1],
[0,2,2],
[0,3,1],
[0,3,2],
[1,1,2],
[1,2,1]   ]
if(coin%5<5):
    a=int(coin/5)  
    b=(a-1)*5     
    d= a-1   
    c=coin-b      
    ab = list[c]
    ab[0] = ab[0] + d
    print(ab)
else:
    a=int(coin/5)  
    b=(a-1)*5     
    d= a-1   
    c=coin-b      
    ab = list[c]
    ab[0] = ab[0] + d
    print(ab)





    

