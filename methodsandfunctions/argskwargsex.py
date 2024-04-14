def myfunc(*args):
    print(args)
    return sum(args) * 0.05

print(myfunc(10 ,20 ,30 ,40 ,50))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'fruit {kwargs['fruit']} is present')
    else:
        print(f'fruit not present')

myfunc( veggie = 'Leaf', milk = 'Cow' , fruit = 'Banana')

def my_food(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I eat {args[1]} {kwargs['food']}")

my_food(3, 2, 4, 5, 6, 8, rice="White", food="eggs", fruit='Banana')

def skyline(input):
    word=''
    for index, letter in enumerate(input):
        if index % 2==0:
            word = word + letter.upper()
        else:
            word = word + letter.lower()
    return word

print(skyline('nagaraja'))
print(skyline('hanuman'))

print("*"*108)
def master_yoda(text):
    mylist = text.split()
    revlist = []
    index= 0
    for index in range(len(mylist)-1, -1, -1):
        revlist.append(mylist[index])
    return " ".join(revlist)

print(master_yoda('I am home'))