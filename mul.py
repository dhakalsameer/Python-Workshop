def multipleBy2(number):
    list = []

    for i in number:
        list.append(i*2)
    return list

nums = [1,2,3,4,5,6]
print(multipleBy2(nums))