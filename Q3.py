a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('Yes, We can.')
else:
    print('No. we cant!')