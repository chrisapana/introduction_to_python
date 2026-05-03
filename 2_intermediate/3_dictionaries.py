client = {
 "name": "Jack Gray",
 "age": 21,
 "isVerified": True
}

print(client['name'])
print(client.get('ban'))
print(client.get('ban', 'hi there'))

print(client.get('age'))


