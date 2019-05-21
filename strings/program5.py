# to check if string anagram or not
a = input('Enter the  string ')
b = input('Enter the string ')
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")
