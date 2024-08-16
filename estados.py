# Lista usando laço for
print(" ")
print("Índice dos estados")
print(" ")

estados = ["São Paulo", "Minas Gerais", "Rio de Janeiro", "Espírito Santo"]

# Listar usando laço com índice 
for i, estados in enumerate(estados, 1):
    print(f"{i} - {estados}")
    print(" ")