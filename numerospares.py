def main():
    # Inicializa a lista com valores de 1 a 10
    lista = list(range(1, 11))
    
    # Filtra e exibe apenas os números pares
    print("Números pares na lista:")
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

if __name__ == "__main__":
    main()
