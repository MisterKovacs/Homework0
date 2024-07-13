a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))
if a == b == c:
    print('3')
elif a == b or b == c or a==c:
    print('2')
else:
    print('0')