def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def main():
    # Solicita os dois números ao usuário
    numero1 = obter_numero("Digite o primeiro número: ")
    numero2 = obter_numero("Digite o segundo número: ")
    
    # Calcula as três somas
    soma1 = numero1 + numero2
    soma2 = numero1 + numero1  # Soma do primeiro número com ele mesmo
    soma3 = numero2 + numero2  # Soma do segundo número com ele mesmo
    
    # Exibe as somas
    print(f"Soma 1 (número1 + número2): {soma1}")
    print(f"Soma 2 (número1 + número1): {soma2}")
    print(f"Soma 3 (número2 + número2): {soma3}")
    
    # Calcula o totalizador
    totalizador = soma1 + soma2 + soma3
    
    # Exibe o totalizador
    print(f"Totalizador das somas: {totalizador:.2f}")

if __name__ == "__main__":
    main()

