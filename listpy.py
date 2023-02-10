# list can contain dublicates, and any data types 

lists = ['name', 1, 2, 3, 1, 'name']

print(lists[5])

lists[5] = 'updatedList'

print(lists)

lists.remove(1)

print(lists)

# del pop and remove we can use delete the element

# adding the and appned the list 

lists.append("apppend element")

print(lists)
# list are mutable data types, we change edit and delete 

# if we want to add moe its to list we can use extand menthod avalable in python 

lst = ['Ramesh', 'Jhande']

lst.extend(["Teju, fjjfj"])

print(lst)

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lst.remove('apple')

print(lst)

print(len(lst))