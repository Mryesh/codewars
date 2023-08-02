def narcissistic(value):
    return value == sum([int(n) ** len(str(value)) for n in str(value)])


narcissistic(115132219018763992565095597973971522400)
#主要是没有理解到什么是以10为基数的narciss number
