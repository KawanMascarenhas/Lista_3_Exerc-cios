def obter_nome():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            return nome
        else:
            print("Nome inválido. Deve ter mais de 3 caracteres. Tente novamente.")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite a idade (entre 0 e 100): "))
            if 0 <= idade <= 100:
                return idade
            else:
                print("Idade inválida. Deve estar entre 0 e 100. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_salario():
    while True:
        try:
            salario = float(input("Digite o salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. Deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_sexo():
    while True:
        sexo = input("Digite o sexo (f ou m): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Sexo inválido. Deve ser 'f' ou 'm'. Tente novamente.")

def obter_estado_civil():
    while True:
        estado_civil = input("Digite o estado civil (s, c, v, d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")

def main():
    nome = obter_nome()
    idade = obter_idade()
    salario = obter_salario()
    sexo = obter_sexo()
    estado_civil = obter_estado_civil()

    print("\nInformações cadastradas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {'Solteiro' if estado_civil == 's' else 'Casado' if estado_civil == 'c' else 'Viúvo' if estado_civil == 'v' else 'Divorciado'}")

if __name__ == "__main__":
    main()
