saldo = 0
extrato = ""

while True:
    print('''
    *********************
        Operações      
    1 - Depositar
    2 - Sacar
    3 - Extrato 
    4 - Sair                  
    *********************
    ''')
    op = int(input("Informe a operação que deseja efetuar"))

    if op == 1:
        while True:
            dp = int(input("Informe o valor para deposito:\n"))
            if dp <=0 and dp:
                dp = int(input("Valor invalido! Informe o valor para deposito:\n"))
            else:
                saldo += dp
                extrato = extrato + f"Deposito = R$ {dp}\n"
                break
    elif op == 2:
        while True:
            vlr_saque = int(input("Informe o valor que deseja sacar:\n"))
            if vlr_saque <= 0:
                vlr_saque = int(input("Valor invalido! Informe o valor que deseja sacar:\n"))
            elif saldo < vlr_saque:
                vlr_saque = int(input("Você não possui saldo suficiente! Informe um valor valor valido para saque:\n"))
            else:
                saldo -= vlr_saque
                extrato = extrato + f"Saque = R$ {vlr_saque}\n"
                break
    elif op == 3:
        print(f"""
            ***********************
            *Extrato
            {extrato}
            *Saldo Atual = R$ {saldo}
            ***********************
            """)
    elif op == 4:
        break
    else:
        print("Operação invalida")
