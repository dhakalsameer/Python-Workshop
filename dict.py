def create_dict(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    print(result)

#converting two lists into a dictionary
create_dict(["a", "b", "c", "d", "e"],[1,2,3,4,5])

