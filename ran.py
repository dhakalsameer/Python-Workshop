# import random
# for i in range(100):
#   print(random.randrange(111111, 999999))



details = {
    'name': "Sameer Dhakal",
    'address': "Ratna chowk",
}

print(details)

details.update({'phone': 9700012127})
print(details)

details.update({'name': "Luffy"})
print(details)

print(type(details['name']))

a = (details.keys())
print(a)
print(type(a))

b= (details.values())
print(b)
print(type(b))

c=(details.items())
print(c)
print(type(c))

