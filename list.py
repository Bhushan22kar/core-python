#create list
fruits=["apple","mango","banana","orange"]
print(fruits)

# Use loop to print list items
# Create a list
numbers = [10, 20, 30, 40, 50]
print("Numbers in the list:")

for num in numbers:
    print(num)

#List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]

print(squares)


#using if-else

numbers = [10, 15, 20, 25, 30]

# Check even or odd numbers
for num in numbers:
    if num % 2 ==0:
        print(num,"is even")
    else:
        print(num,"odd num")