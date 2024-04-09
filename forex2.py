nums = [1,2,3,4,5,6,7,8,9,10]

for num in nums:
    if num%2==0:
        print(num)
    else:
        print(f"odd num:{num}")

print("*"*21)
list_sum=0
for num in nums:
    list_sum = list_sum + num
print(list_sum)

print("*"*21)
word="Hello World"
for letter in word:
    print(letter)

print("*"*21)
tupnum = (1,2,3)
for num in tupnum:
    print(num)
print("*"*21)
##tuple unpacking
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in my_list:
    print(a)
    print(b)
    print(c)

print("*"*21)
my_dict= {'k1':1, 'k2':2, 'k3':3}
for item in my_dict:
    print(item)
for item in my_dict.items():
    print(item)
for key,value in my_dict.items():
    print(key)
    print(value)
for value in my_dict.values():
    print(value)
