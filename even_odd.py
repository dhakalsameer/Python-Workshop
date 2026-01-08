def even_odd(number):
    even = []
    odd = []

    for i in number:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd
    
nums = [1,3,4,3,2,4,5,6,7,8]

even_list, odd_list = even_odd(nums)
print(even_list)
print(odd_list)
