# List Comprehension is a pythonic way to do stuff in one line

def div7():
    l1 = [23, 43, 53, 24, 44, 54]
    mylist1 = []
    for i in l1:
        mylist1.append(i/7)
    
    return mylist1

print(div7())


## By using LC

l2 = [21, 243, 1234, 23421]

qwe = [i/7 for i in l2]

print(qwe)


## Filtering by using LC

l2 = [566, 650, 56, 98, 65, 85, 45, 75, 63, 45, 65, 145, 789]

div_5 = [x for x in l2 if x%5==0]

print(div_5)
