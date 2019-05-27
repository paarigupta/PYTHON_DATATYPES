# Multiply of matrices

a = []
b = []
ans = []
c1=int(input("Enter no. of columns of first matrix: "))
r1=int(input("Enter the rows of first matrix: "))
c2=int(input("Enter the columns of second matrix: "))
r2=int(input("Enter the rows of second matrix: "))

if c1 == r2:
    print("Enter the elements of first matrix:")
    for i in range(0,r1):
        t = []
        for j in range(0,c1):
            p=int(input())
            t.append(p)
        a.append(t)
    print("The matrix is: ")
    print(a)

    print("Enter the elements of second matrix:")
    for i in range(0,r2):
        t = []
        for j in range(0,c2):
            t.append(int(input()))
        b.append(t)
    print("The matrix is: ")
    print(b)

    for i in range(0,r1):
        t = []
        for j in range(0,c2):
            t.append(0)
        ans.append(t)

    for i in range(0,r1):
        for j in range(0,c2):
            for k in range(0,r2):
                     ans[i][j]+=a[i][k]*b[k][j]
    print("Multiplication is: ")
    print(ans)
else:
    print("Multiplication is not possible.")
