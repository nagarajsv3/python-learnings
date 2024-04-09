my_set = set()
print(my_set)
print(type(my_set))

my_set.add(1)
my_set.add("Hi")
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set)

my_list = [1,2,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
my_set = set(my_list)
print(my_set)

print(set("mississippi"))