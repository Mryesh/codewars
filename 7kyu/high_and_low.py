def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return " ".join([str(max(nums)), str(min(nums))])


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
