

listex = ["Joey","Chandler","Ross","Monika","Pheobe","Rachel",1,True]
print(listex)

friends = ["Joey","Chandler","Ross","Monika","Pheobe","Rachel"]

print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[-3])

print(friends[1:])
print(friends[1:3])

friends[1] = "Late Chandler"
print(friends[1])
print(friends)
friends[1] = "Chandler"
print(friends)

lucky_numbers = [3,6,9,12,15,18,21,24]
friends.extend(lucky_numbers)
print(friends)
friends = ["Joey","Chandler","Ross","Monika","Pheobe","Rachel"]

friends.append("Bond")
friends.insert(1, "Dhoni")
print(friends)

friends.remove("Dhoni")
print(friends)

friends.pop()
print(friends)

print(friends.index("Pheobe"))
print(friends.index("Ross"))
#print(friends.index("Sachin"))

friends.append("Ross")
print(friends.count("Ross"))
friends.sort()
print(friends)

lucky_numbers = [2, 1, 3, 4, 6, 5]
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [2, 1, 3, 4, 6, 5]
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)