my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict["key1"])
print(my_dict["key2"])

my_dict = {'key1' : 'value1' , 'letterlist' : ['a','b','c'], 'nesteddict' : {'apple': 2.99, 'banana' : 1.99, 'milk':3.99}}
letter = 'c'
print(letter.upper())
print(my_dict['letterlist'][2].upper())
print(my_dict['nesteddict']['apple'])
print(my_dict['nesteddict']['milk'])

dic = {'k1':100, 'k2':200}
dic['k3'] = 300
print(dic)
dic['k2'] = 2000
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

