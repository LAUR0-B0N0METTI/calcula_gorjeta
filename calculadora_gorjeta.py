def calculadora_de_gorjeta():
    print("Bem-vindo à Calculadora de Gorjeta!")

    # Solicitar o valor da conta ao usuário com manipulação de exceções
    while True:
        try:
            valor_conta = float(input("Informe o valor da conta: R$ "))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    # Solicitar a porcentagem de gorjeta ao usuário com manipulação de exceções
    while True:
        try:
            percentual_gorjeta = float(input("Qual a porcentagem de gorjeta que você deseja deixar? "))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido para a porcentagem de gorjeta.")

    # Calcular o valor da gorjeta e o total a ser pago
    valor_gorjeta = (percentual_gorjeta / 100) * valor_conta
    total_pagar = valor_conta + valor_gorjeta

    # Solicitar ao usuário se deseja arredondar o total
    arredondar = input("Deseja arredondar o total a pagar? (S/N): ").upper()

    if arredondar == "S":
        total_pagar = round(total_pagar)

    # Exibir os resultados
    print("\nResumo:")
    print(f"Valor da Conta: R$ {valor_conta:.2f}")
    print(f"Gorjeta ({percentual_gorjeta}%): R$ {valor_gorjeta:.2f}")
    print(f"Total a Pagar: R$ {total_pagar:.2f}")

# Chamar a função principal
calculadora_de_gorjeta()
