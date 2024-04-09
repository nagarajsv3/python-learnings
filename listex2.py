my_list = [1,2,3]
print(my_list)

my_list = ["one", 2, 3.0, False]
print(my_list)

my_list = [1, 2, 3]

another_list = [4, 5, 6]

#Combine lists / concatenate lists
comb_list = my_list + another_list
print(comb_list)

#indexing
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[0])
print(my_list[1])

#slicing
print(my_list[2:7])
print(my_list[2:7:2])

#mutate list
my_list[0] = 99
print(my_list)

#len
print(len(my_list))

my_list.append(10)
my_list.append(11)
print(my_list)

popped_item = my_list.pop()
print(popped_item)
print(my_list)

popped_item = my_list.pop(0)
print(popped_item)
print(my_list)

#sort() - modifies list inplace. No return type
my_list = ["a", "e", "b", "x", "c"]
#sorted_list = my_list.sort() #Wrong
my_list.sort()
print(my_list)
print("*"*21)

num_list = [10, 2, 99, 1, 5, 3, 0, 104]
print(num_list)
num_list.sort()
print(num_list)

#reverse() - reverses the list inplace. No return type
num_list.reverse()
print(num_list)