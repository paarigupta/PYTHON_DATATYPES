#Lambda function

l1 = [4,7,9,7]
print(l1)
l2 = [8,9,7,0,8]
print(l2)

l3 =[list(map(lambda a,b:a+b,l1,l2))]
print(l3)
