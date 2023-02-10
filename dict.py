name = {
    'name': 'book',
    'price' : '30.34'
}

print(name['name'])

#delete the lements form dict 


# del(name['name'])

# print(name)
#another way is use pop

print( name.pop('name'))

# add new item 

name['name'] = 'New Book'

# to update the dict is update the dict 

name.update({'name1' : 'new Book 1'})
print(name.get('nam1', 0))  # 0 is call back value if you dont get the name1 then 0 will return 
print(name.get('nam', 0)) # get will return the call back value 

print(name)

item = {
    "title": "Bread",
    "price": 1.6,
    "quantity": 4,
}

amount = item['price'] * item['quantity']

item['amount'] = 10

print(item)