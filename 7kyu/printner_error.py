def printer_error(s):
    lens = len(s)
    count_error = 0
    list1 = list(s)
    color = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

    for element in list1:
        if element in color:
            continue
        else:
            count_error += 1

    return f"{count_error}/{lens}"


s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s)
#还是不够简便
