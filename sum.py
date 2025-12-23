# def sum(a, b,c):
#    print("sum of the numbers", a+b+c)

# add = sum(2,7,8)
# print(add)

# def sum(a,b,c,d):
#     print("sum of the numbers", a+b+c+d)

# function overriding ma error aauxa , euta object ko lagi matra target garxa
# sum(10,10,20)
# sum(2,5,6,7)


# args is tuple
# def add(* args):
#     print(args)
#     print(type(args))


# add(1,2,3)
# add(1,2,3,4)
# add([1,2,3,4])

# def tup(* args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(f"Sum of {len(args)} numbers is {sum}")

# tup(1,2,3,4)

def operation(operator, * args):
    sum = 0
    mul = 1
    if(operator == "+"):
        for i in args:
            sum = sum + i
        print(f"Sum of {len(args)} numbers is {sum}")
    elif(operator == "*"):
        for i in args:
            mul = mul * i
        print(f"Multiplication of {len(args)} numbers is {mul}")

operation("+", 1,2,3,4,5)
operation("*", 1,2,3,4,5)
operation("*", 4,5,6,7,8,9)
operation("+", 3,6,7,8,9)


def details(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    print(kwargs.items())
    print(kwargs.values())
    print(kwargs.keys())

details(name="Gandaki Uni", estd=2019)
details(name="TU",chancellor="PM",estd=1959)
details(name="PU",chancellor="PM",estd=1991)
