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
#String to list
number=input().split()
print(number)