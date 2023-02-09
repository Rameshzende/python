# how to react multi line in python
multiQuote = 'Hi, I am  learning Python """", and it`s very easy " '
print(multiQuote)

# to print the multi line use trible quotes 
multi = """ 
  Hye, this Ramesh Jhande, 
  learning python.
"""
print(multi)


# sting 

name = 'Ramesh Jhande'
print(name.upper(), 'R')
print(name.count('R'))
print(name)
print(name[0:6])
print(name[7:])
print(name[0:len(name)]) # form 0 index to last

print(name[-3:])

inputName = input('Enter name :')

if len(inputName) > 3:
    print(inputName, 'is lenght is greate that 3 latters')
else:
    print(inputName, 'is lenght is less the 3 letters')