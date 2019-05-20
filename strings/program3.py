# Check if string pallindrom or not

str = input('Enter the string ')
my_str = ''
for i in str:
    my_str = i + my_str
if str == my_str:
    print("Pallindrome")
else:
    print("Not Pallindrome")
    
