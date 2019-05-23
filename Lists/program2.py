# Addition of matrix

a = []
b = []
r = int(input("Enter the rows of matrix: "))
c = int(input("Enter the column of matrix: "))

print("Enter the elements of first matrix: ")
for i in range(0,r):
    t = []
    for j in range(0,c):
        p=int(input())
        t.append(p)
    a.append(t)
print("First matrix is: ")
print(a)

print("Enter the elements of second matrix: ")
for i in range(0,r):
    t = []
    for j in range(0,c):
        p=int(input())
        t.append(p)
    b.append(t)
print("Second matrix is: ")
print(b)

ans = []
for i in range(0,r):
    t = []
    for j in range(0,c):
        t.append(0)
    ans.append(t)

for i in range(0,r):
    for j in range(0,c):
        ans[i][j]+=a[i][j]+b[i][j]
print("Addition is: ")
print(ans)
    







