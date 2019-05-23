# Transpose of Matrix

a = []
b = []
r = int(input('Enter no. of rows: '))
c = int(input('Enter no. of column: '))

print("Enter the elements of matrix: ")
for i in range (0,r):
    t=[]
    for j in range(0,c):
        p = int(input())
        t.append(p)
    a.append(t)
print("The matrix is: ")
print(a)

for i in range (0,c):
    t=[]
    for j in range(0,r):
        t.append(0)
    b.append(t)
for i in range (0,c):
    for j in range(0,r):
        b[i][j] = a[j][i]
print("The transpose matrix is: ")
print(b)


