from re import split
import re

def Add(numbers):

    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")
    if numbers.endswith(",") or numbers.startswith(","):
        return "error"

    if numbers.find(",,") < -1:
        return "error"

    tmpNumbers = numbers.split(",")

    sum = 0
    for num in tmpNumbers:
        sum += int(num)

    return sum

x = Add("1,3,5")
print(x)
