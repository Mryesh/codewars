def narcissistic(value):
    return value == sum([int(n) ** len(str(value)) for n in str(value)])


narcissistic(115132219018763992565095597973971522400)
#借鉴
