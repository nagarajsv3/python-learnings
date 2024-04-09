nums = [1,2,3,4]

for num in nums:
    pass #Do nothing

for num in nums:
    if num==2:
        continue
    print(num)

word = "Hello World"
for letter in word:
    if letter == 'l':
        continue
    print(letter)

print("*"*21)
word = "Hello World"
for letter in word:
    if letter == 'l':
        break
    print(letter)

x=0
while x < 100 :
    if x ==4:
        break 
    print(x)
    x +=1
