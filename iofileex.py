my_file = open("myfile.txt")
#open("unknownfile.txt") #FileNotFoundError: [Errno 2] No such file or directory: 'unknownfile.txt'

print(my_file.read())
print("*"*21)
print(my_file.read())
print("*"*21)
my_file.seek(0)
print(my_file.read())

my_file.seek(0)
contents = my_file.read()
print(contents)
print("*"*21)

my_file.seek(0)

print(my_file.readlines())
my_file.close()
print("*"*21)

with open('myfile.txt') as my_file2:
    content2 = my_file2.readlines()

print(content2)

with open('myfile.txt', mode='r') as f:
    print(f.readlines())

with open('myfile2.txt', mode='w') as f:
    print(f.write("New file got created"))

with open('myfile2.txt', mode='a') as f:
    print(f.write("\n2nd line"))
    print(f.write("\n3rd line"))

print("*"*21)
with open('myfile2.txt', mode='r+') as f:
    print(f.readlines())



