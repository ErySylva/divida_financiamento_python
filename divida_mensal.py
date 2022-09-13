"""Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
Pergunte também o valor mensal que será pago. Imprima o número de meses para que
a dívida seja paga, o total pago e o total de juros pago."""

valor_divida = float(input("Digite o valor da dívida: "))
juro_mensal = float(input("Juros mensal: "))
valor_mensal = float(input("Valor mensal: "))
contagem = 0

while contagem <= 24:  #Loop de 24 vezes (meses)

    valor = valor_divida + (valor_divida * (juro_mensal / 100))  #valor do juros calculado de acordo com a entrada do usuário, e sendo acrescentado no valor da divida.
    
    valor_divida = valor  #acrescentando no valor inicial

    print(f"Em {contagem} meses, valor divida acrescentado {valor_divida:.3f}")  
    total_juros = juro_mensal * contagem  #Realizando o calculo de 24 meses sobre o juros inicial  
    contagem += 1  #Acrescentando no while

    if contagem >= 24:  #Quando o valor chegar maior ou igual a 24, realizar o if 
        meses = valor_divida / valor_mensal  #Dependendo do valor a ser pago mensalmente, ira realizar a contagem de meses para quitar a divida. 
        
        print(f"Valor quitado em meses é: {meses:.1f}")
        print(f"Total de Juros pago nesse periodo {total_juros:.2f}% juros em {contagem} meses")
        break
