# Lambda function in list comprehension

l=list(map(int,input().split()))
l1 = []
l1 = [(lambda x:x**2)(x) for x in l]
print(l1)
