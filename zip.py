names = ["Ram", "Shyam", "Mohan"]    #to combaine two list we can use zip
ages = [20, 21, 22]
cities = ["Pune", "Mumbai", "Delhi"]

for names,ages,cities in zip(names, ages ,cities):
    print(names,ages,cities)