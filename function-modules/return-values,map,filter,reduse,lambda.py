#return value


def add(a, b):
    return a + b       #return value to the function

# Store returned value
result = add(10, 20)

# Print result
print("Sum =", result)


#lambda

square = lambda x: x * x  #anonymus function means without name

print(square(5))


add = lambda a, b: a + b

print(add(10, 20))

#map

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))  #map applies a function to all items in a list.

print(result)



#filter

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))  #selects values based on a condition.

print(even)



#reduce

from functools import reduce

numbers = [1, 2, 3, 4]              #educe() is used to reduce a list into a single value.

result = reduce(lambda x, y: x + y, numbers)

print(result)