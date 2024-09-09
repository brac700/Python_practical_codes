n = 5

print(f"\n7.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

print(f"\n8.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print(f"\n9.")

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print(f"\n10.")

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print('*', end='')
    print()
    
