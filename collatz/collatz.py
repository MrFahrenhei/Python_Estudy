def collatz(conjecutre):
    while conjecutre > 1:
        print(conjecutre, end=' ')
        if (conjecutre % 2):
            conjecutre = 3 * conjecutre + 1
        else:
            conjecutre = conjecutre // 2
    print(1, end='')

n = int(input('Insira o valor: '))

print('Sequência: ', end='')

collatz(n)
