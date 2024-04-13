# Resposta para o desafio v1. do Bootcamp Bootcamp Coding The Future Vivo - Python AI Backend Developer
# Objetivo: Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
# As regras de negócio das operações estão descritas no README.md do repositório no gitHub
# https://github.com/toniacprado/DIO-Python-AI-Backend-Developer-Desafio-Sistema-Bancario-v1
# Autor: Toni A C Prado

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0.0
limite = 500
extrato = f"Saldo Inicial: R$ {saldo:.2f}\n"
numero_saques = 0
LIMITE_SAQUES = 3


# Função para tratar os inputs e aceitar somente entrada de valores numéricos
def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, digite um número válido.")


print("================ Bem-vindo ao The Bootcamp Bank =================\n")
while True:
    print("\nSelecione uma opção: ")
    opcao = input(menu)

    if opcao.upper() == "D":
        valor = input_float("Digite um valor a depositar: ")
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Entrada inválida, favor digitar um valor numerico positivo a ser depositado")
    elif opcao.upper() == "S":
        if numero_saques < LIMITE_SAQUES:
            valor = abs(input_float(f"O limite por saque é R$ {limite:.2f}. Digite o valor que deseja sacar: "))
            # a função abs vai tratar e validar para que independente do sinal digitado pelo usuário ele faça o débito no saldo corretamente.
            
            if valor > limite:
                print(f"Valor inválido, o máximo permido por saque é de R$ {limite:.2f}. ")
            elif valor > saldo:
                print(f"Saldo insuficiente para este valor de saque! Saldo disponível R$ {saldo:.2f}. ")
            elif valor > 0:
                print("Saldo concluído com sucesso!")
                saldo -= valor
                numero_saques +=1
                extrato += f"Saque:  -R$ {valor:.2f}\n"
        else:
            print(f"Limite máximo de {LIMITE_SAQUES} saques atingidos.")
    elif opcao.upper() == "E":
        print("\n================ EXTRATO =================")
        print(extrato)
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao.upper() == "Q":
        print("The Bootcamp Bank agradece a sua visita, volte sempre!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
