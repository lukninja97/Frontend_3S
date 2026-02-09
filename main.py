from Time import Time

time = Time()

print("")
print("Bomba Patch")
print("Cem por cento atualizado. É ruim de aturar. Bomba patch virou moda. Todo mundo quer jogar.")

while True:

    print("")
    print("Escolha uma opção")
    print("1 - Criar time")
    print("2 - Jogar")
    print("3 - Ver time")

    opcao = input("")

    if opcao == "1":
        time.cadastrar()
    elif opcao == "2":
        time.jogar()
    elif opcao == "3":
        time.apresentar()
    else:
        break
