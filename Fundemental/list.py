
list1=[1,2,3,4,5,4,7]
list2=['Banana','Apple','Mango','Orange']
list3=list2.copy()

list1.sort()
#list2.reverse()
list1.extend(list2)
list2.insert(1, 'Cherry')
list2.pop(2)
list1.remove(value)


print(list2.index('Cherry'))
print(list2.count('Mango'))
print(list1)
print(list2)
print(list3)
