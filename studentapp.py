from Student import Student

arjun = Student("arjun", "Archery", 9.9, True)
bheem = Student("bheem", "Gadha", 9.9, True)
hanuman=Student("hanuman", "all", 10, True)
harry=Student("harry", "earthing", 4, True)

print(arjun.name+" has taken "+arjun.major)
print(bheem.name+" has taken "+bheem.major)
print(hanuman.name+" has taken "+hanuman.major)

print(hanuman.on_honor_roll())
print(harry.on_honor_roll())
