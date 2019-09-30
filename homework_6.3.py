def wrap(string, width):
    list_2 = []
    for num, element in enumerate(string):
        if (num + 1) % width == 0:
            list_2.append(f"{element} \n")
        else:
            list_2.append(element)
    list_2 = "".join(list_2)
    return list_2


print(wrap("TheBestPlayerOfTheMonth", 4))
