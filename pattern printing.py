# Using loops print the following pattern
"""
1.  1               2.  1               3.  1               4.      1           5.    1
    12                  12                  10                     12                1 2
    123                 123                 101                   123               1 2 3
    1234                1234                1010                 1234              1 2 3 4
    12345               12345               10101               12345             1 2 3 4 5
    12345               1234
    1234                123
    123                 12
    12                  1
    1
"""
n = int(input("Enter the value of n: "))
# Pattern 1
print("*****First Pattern*****")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(i+1-j, end='')
    print()

# Pattern 2
print("*****Second Pattern*****")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
for i in range(n, 0, -1):
    for j in range(i - 1, 0, -1):
        print(i - j, end='')
    print()

# Pattern 3
print("*****Third Pattern*****")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:      # since even places has to be zero
            print("0", end='')
        else:
            print("1", end='')
    print()

# Pattern 4
print("*****Fourth Pattern*****")
for i in range(1, n + 1):
    print((n-i)*" ", end='')
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Pattern 5
print("*****Fifth Pattern*****")
k = n-1                    # variable for number of spaces
for i in range(1, n+1):
    for j in range(1, k+1):
        print(end=' ')      # print spaces
    k = k - 1
    for j in range(1, i+1):
        print(j, "", end='')
    print()