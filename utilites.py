def find_max(numbers):
    maxnumber = numbers[0]
    for items in numbers:
        if maxnumber < items:
            maxnumber = items
    return maxnumber
