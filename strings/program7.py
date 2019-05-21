# To check the string panagram or not

a = input("Enter the string ")
str ='abcdefghijklmnopqrstuvwxyz'
a.lower()
for i in str:
    if i in a:
        continue
    else:
        print("Not panagram")
        break
else:
    print("Panagram")
