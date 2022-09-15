# a, b,  *d = 'room'
# print(a, b, d)


# a, *b = 'room'
# print(a, b)


for i in range(5):
    for j in range(5 - i):
        print('*', end='')
    print()
