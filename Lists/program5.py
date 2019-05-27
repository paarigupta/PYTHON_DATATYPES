#List Comprehension

l=list(map(int,input().split()))
new_list = []
new_list = [i**2 for i in  l]
print(new_list)
