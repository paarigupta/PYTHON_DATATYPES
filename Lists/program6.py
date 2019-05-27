#if else in list comprehension

l1 = [i for i in range(0,101) if i%2 == 0]
print(l1)

l2=[1 if i%2==0 else 0 for i in range(1,101)]
print(l2)
