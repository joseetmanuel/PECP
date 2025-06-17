numbers = [1,1,2,3]
try:
    numbers[0:1]
    print("numbers[0:1]")
except:
    pass

try:
    numbers[6]
    print("numbers[6]")
except:
    pass

try:
    numbers[-10]
    print("numbers[-10]")
except:
    pass

try:
    numbers[numbers[3]]
    print("numbers[numbers[3]]")
except:
    pass