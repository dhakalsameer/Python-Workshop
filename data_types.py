a=10
print(type(a))

b ="Nepal"
print(type(b))

c=True
print(type(c))

d =[1,2,3,4,5]
print(type(d))

# tuple ma define garyesi change garna mildaina
e =(1,2,3,4,5)
print(type(e))

# duplicate value huna payena in the set
f ={8,9,10,14}
print(type(f))


# Dictionary
g = {
    'name': "sameer",
    'address': "rastra"
}
print(type(g))


h = range(10)
print(type(h))


for k in range(1, 40, 5):
    print(k)

i = input("Enter a integer:")
j = int(i)

if(j == 0):
    print("It is zero")
elif(j < 0):
    print("It is negative integer")
else:
    print("It is positive integer")