def str(string):
    list = []

    for l in string:
        if len(l) > 5:
            list.append(l)
    return list

words = ["Luffy", "CR7", "Sau", "Saugat", "Bandre", "Samita"]
print(str(words))