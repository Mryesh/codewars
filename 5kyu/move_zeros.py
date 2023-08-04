def move_zeros(lst):
    lay = get_index(lst, 0)
    for i in lay:
        del lst[i]
        lst.append(0)
        for w in range(0, len(lay)):
            lay[w] -= 1
    return lst


def get_index(lst=None, item=0):
    return [i for i in range(len(lst)) if lst[i] == item]
