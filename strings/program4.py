# remove punctuation from string

str1 = input()
punctuation = ''' !@#$%^&*()_:+-="';<>.,/?\|[]{}`~ '''
str =' '
for i in  str1:
    if i not in punctuation:
        str = str + i
print(str)
