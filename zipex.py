my_list1 = [1,2,3,4]
my_list2 = ["Mangala", "Naveen", "Smita", "Nagaraja"]
my_list3 = [10,20,30,40]

for item in zip(my_list1, my_list2, my_list3):
    print(item)
    print("\n")

for a,b,c in zip(my_list1, my_list2, my_list3):
    print(a)
    print(b)
    print(c)
    print("\n")

ziplist = list[zip(my_list1, my_list2, my_list3)]

