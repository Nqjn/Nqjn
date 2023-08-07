mylist = [2,7,11,13,15,18,9,10]

for i in range(len(mylist)-1):
    for l in range (len(mylist)-i-1 ):
        if mylist[i] + mylist[l +1 +i ] == 22:
            print(f"{mylist[i]} + {mylist[l + 1+ i]} = 22")
            
            