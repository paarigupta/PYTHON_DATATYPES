# To separate given string in two substring in uppercase and in lowercase
a = input("enter the string")
s1 = ''
s2 = ''
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        s1=s1+i
    else:
        s2=s2+i
print(s1)
print(s2)
