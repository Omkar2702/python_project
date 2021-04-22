n = int(input("Enter the value of n: "))
b = int(input("Enter 0 or 1: "))
b = bool(b)
if b == True:
    for i in range(1, n + 1):
        print(i*"*")
else:
    for i in range(1, n + 1):
        print((n+1-i)*"*")
