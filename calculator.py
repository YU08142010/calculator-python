a = int(input('最初の数字は何ですか >>'))
b = int(input('最後の数字は何ですか >>'))
c = input('記号は何ですか +|-|*|/ >>')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('error')
