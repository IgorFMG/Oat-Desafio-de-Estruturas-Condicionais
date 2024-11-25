def calc_reajust(sal_atual):
    inf = 3.8 / 100

    if sal_atual <= 280:
        percentual = 20
    elif sal_atual <= 700:
        percentual = 15
    elif sal_atual <= 1500:
        percentual = 10
    else:
        percentual = 5

    valor = sal_atual * (percentual/ 100)
    nov_sal = sal_atual+ valor
    aumento_valor = valor * (1 - inf)


    print(f"Salario antes do reajuste é igual: R$ {sal_atual:.2f}")
    print('---------------------------------------------------')
    print(f"Percentual de aumento aplicado: {percentual}%")
    print('---------------------------------------------------')
    print(f"Valor adicional: R$ {valor:.2f}")
    print('---------------------------------------------------')
    print(f"Novo salario , apos o aumento: R$ {nov_sal:.2f}")
    print('---------------------------------------------------')
    print(f"Valor depois do reajuste, descontado a inflação: R$ {aumento_valor:.2f}")

    salario_atual = float(input("Digite o salario atual: "))
    calc_reajust(salario_atual)
