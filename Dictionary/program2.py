#concatenation of dictionaries
dict1= {1:10,2:20}
dict2= {3:30,4:40}
dict3= {}
for d in (dict1,dict2):
    dict3.update(d)
print(dict3)
