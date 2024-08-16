def main():
    # Cabeçalho da tabela
    print("Nro\tQuadrado\tCubo")
    
    # Calcula e exibe os quadrados e cubos dos números de 0 a 50
    for nro in range(51):
        quadrado = nro ** 2
        cubo = nro ** 3
        
        # Impressão dos resultados com tabulação para separação
        print(f"{nro}\t{quadrado}\t{cubo}")

if __name__ == "__main__":
    main()
