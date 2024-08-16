def exibir_menu():
    print("Menu:")
    print("1")
    print("2")
    print("3")

def obter_opcao():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        if opcao in ['1', '2', '3']:
            return opcao
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

def exibir_mensagem(opcao):
    if opcao == '1':
        print("Eu estou estudando Python!")
    elif opcao == '2':
        print("Eu estou estudando PHP!")
    elif opcao == '3':
        print("Eu estou estudando Java!")

def main():
    opcao = obter_opcao()
    exibir_mensagem(opcao)

if __name__ == "__main__":
    main()



