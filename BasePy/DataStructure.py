"List"
myList1=[1,2,3,"Apple"]
myList2=([2,3,4])
myList1+=myList2
print(myList1)
myList1.extend([2,3,4])
print(myList1)
print([i*i for i in range(1,6)])
myList1.append(3)
print(myList1[4])
myList1.remove(3)
myList1.pop()
myList1.insert(2,20)
print(max(myList2))
print(min(myList2))
myList3=sorted(myList2)
print(myList3)
"String to list"
number=input().split()
print(number)
"Tupples"
'''
1.Immutable
2.in () seperated by ','
3.ex=(1,"Hello",7)
4.Faster than list
5.tupple to list
    l=list(tupple)
6.list to tupple
    t=tupple(l)
7.Functions
    max(),min(),len()
'''
#Dictionary
'''
1.Hash Maps
d={"key":value,"mango":1}
'''
d={"Apple":1,"Mango":2}
print(type(d))
print(d)
print(d["Mango"])
d["Guava"]=3
d["Guava"]=[4,5]
print(d.keys())
print(d.values())
d.get("Mango")
if "Mango" in d:
    print(d.items())
    l=list(d.items())