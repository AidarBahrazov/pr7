print('Введите целое положительное простое число для перевода в двоичную и восьмеричную систему счисления')
x=input()
if x.isdigit():
    z=bin(int(x))
    print(f'Число {x} в двоичной состеме счисления: {z[2:]}')
    v=oct(int(x))
    print(f'Число {x} в восьмиричной состеме счисления: {v[2:]}')
else:
    print('Введите целое положительное простое число для перевода, программа переводит только их')
