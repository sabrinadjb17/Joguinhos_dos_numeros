print('Bem-vindo ao Joguinho dos Números! 🎯')
print('Digite números positivos. Digite 0 para sair.')

soma = 0

while True:
    entrada = input('Número: ')

    if entrada == '':
        print('⚠️ Entrada vazia ignorada.')
        pass
        continue

    num = int(entrada)

    if num == 0:
        print('Jogo concluído!')
        break

    elif num > 0 and num <= 1000:
        soma += num

    elif num < 0:
        print('❌ Número negativo ignorado!')
        continue

    elif num > 1000:
        print('🚨 Número muito alto! Jogo encerrado.')
        break

print(f'Soma total dos números válidos: {soma}')
