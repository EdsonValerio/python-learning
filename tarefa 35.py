r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O triangulo pode ser formado!! ', end='')
    if r1 == r2 == r3:
        print('Triangulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Triangulo ESCALENO')
    else:
        print('Triangulo ISÓCELES')
else:
    print('O triangulo NÃO pode ser formado!!')
