import random
def randInt(min=0, max=100):
    num = random.randrange(min,max)
    return num

print("--------If no arguments are provided, the function should return a random integer between 0 and 100.-------")
print(randInt())
print("--------If only a max number is provided, the function should return a random integer between 0 and the max number.-----------------")
print(randInt(max=40))
print("--------If only a min number is provided, the function should return a random integer between the min number and 100-----------------")
print(randInt(min=20))
print("--------If both a min and max number are provided, the function should return a random integer between those 2 values.-----------------")
print(randInt(min=1,max=10))