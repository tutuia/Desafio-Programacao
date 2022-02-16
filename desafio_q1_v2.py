while True:
    try:
        n = int(input('Informe o tamanho da escada: '))
        if n >= 0:
            break
        else:
            print('entrada invalida. Informe um inteiro positivo.\n')
    except:
        print('entrada invalida. Informe um inteiro positivo.\n')
 
for count in range(n+1):
    print(((n-count)* ' ') + (count * '*'))

