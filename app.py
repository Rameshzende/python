contact = {
    'ramesh' : 45,
    'umesh' : 46,
    'jhande' : 47
}

client = input('Search for name    ')

if client in contact:
    print(client, contact[client]);
else:
    print('No client Found')
