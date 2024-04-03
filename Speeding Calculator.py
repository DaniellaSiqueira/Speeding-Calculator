velocidade = int(input('Qual a velocidade que o carro estava?: '))
multa = velocidade - 110
multa_= multa * 5
if velocidade <= 110:
    print ('Você não foi multado!')
if velocidade >= 110:
    print (f'Você foi multado no valor de R$: {multa_} ')
