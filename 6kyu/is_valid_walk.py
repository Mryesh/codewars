def is_valid_walk(walk):
    o_point = [0, 0]
    times = len(walk)
    for i in walk:
        if i == 'n':
            o_point[0] += 1
        elif i == 's':
            o_point[0] -= 1
        elif i == 'e':
            o_point[1] += 1
        else:
            o_point[1] -= 1
    if o_point == [0, 0] and times == 10:
        return True
    else:
        return False
