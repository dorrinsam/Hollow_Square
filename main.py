a = int(input())
b = int(input())

if a < b:
    print('Wrong order!')
elif ((a - b) % 2) == 1:
    print("Wrong difference!")
elif a == b:
    print('Wrong order!')
else:
    for i in range(a):
        for j in range(a):
            if i >= a - ((a - b) / 2) or j >= a - ((a - b) / 2) or j == a - 1 or i < ((a - b) / 2) or j < (
                    (a - b) / 2):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
