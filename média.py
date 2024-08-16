def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    notas = []
    
    for i in range(1, 5):
        nota = obter_nota(f"Digite a {i}ª nota (entre 0 e 10): ")
        notas.append(nota)
    
    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")

if __name__ == "__main__":
    main()
