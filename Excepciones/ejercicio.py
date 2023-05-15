frase = input("Digite una frase: ")
letra = input("Digite que letra quiere buscar: ")
contador = 0

for i in frase:
    if i == letra:
        contador+=1

print(contador)
