# To make dictionary by given tuple

# if only tuple is given

t = ('key1' , 'key2' , 'key3')
my_dict = dict.fromkeys(t)
print(my_dict)

# if list is given

y = [1,2,3]
my_dict = dict.fromkeys(t,y)
print(my_dict)
