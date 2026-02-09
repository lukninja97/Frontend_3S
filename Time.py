import random


class Time:
    def __init__(self, nome="", treinador="", torcedores=0, renda=0, pontos=0):
        self.nome = nome
        self.treinador = treinador
        self.torcedores = torcedores
        self.renda = renda
        self.pontos = pontos

    def cadastrar(self):
        self.nome = input("Qual o nome do time ")
        self.treinador = input("Qual é o treinador do time ")

        print("")

        print(f"Parabens você criou o time {self.nome}")
        print("Suas informações")
        print("Treinador", self.treinador)
        print(self.torcedores, "Torcedores")
        print("Renda R$", self.renda)
        print(self.pontos, "Pontos")

    def apresentar(self):
        print("-"*20, self.nome, "-"*20)
        print("Torcedores", self.torcedores)
        print(f"Renda R$ {self.renda}")
        print("Pontos", self.pontos)

    def jogar(self):
        venceu = random.randint(0, 1)

        if venceu == 1:
            self.torcedores = self.torcedores + 5
            self.renda = self.renda + 10000
            self.pontos = self.pontos + 3

            print("")
            print("Você ganhou!")
            print("Resultados")
            print("Aumentou 5 Torcedores")
            print("ganhou 3 Pontos")
            print("Ganhou R$10.000,00")
            print("")
        else:
            self.torcedores = self.torcedores - 1
            self.renda = self.renda - 1000
            self.pontos = self.pontos - 3

            print("")
            print("Você perdeu")
            print("Resultados")
            print("Diminuiu 1 torcedor")
            print("Perdeu 3 Pontos")
            print("Perdeu R$1.000,00")
            print("")

