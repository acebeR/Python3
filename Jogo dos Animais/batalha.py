import classes

def batalha(animal1, animal2):
    print(f"\n⚔️ {animal1.nome} VS {animal2.nome} ⚔️")
    while animal1.vida > 0 and animal2.vida > 0:
        dano1 = animal1.atacar()
        animal2.tomar_dano(dano1)

        if animal2.vida <= 0:
            break

        dano2 = animal2.atacar()
        animal1.tomar_dano(dano2)

    if animal1.vida > 0:
        print(f"\n🏆 {animal1.nome} venceu!")
    else:
        print(f"\n🏆 {animal2.nome} venceu!")

def validaQuemEQuem(animal,life):
    if(animal.lower() == "leao"):
        return classes.Leao("Leão", life)
    if(animal.lower() == "cobra"):
        return classes.Leao("Cobra", life)
    if(animal.lower() == "aguia"):
        return classes.Leao("Águia", life)

# Lendo do usuario
print("==========================")
leitura1 = input("Quem é o animal 1? ")
leitura2 = input("Quem é o animal 2? ")
print("==========================")

vida1= int(input("Quanto de vida "+ leitura1+ " possui? "))
vida2 = int(input("Quanto de vida "+ leitura2+ " possui? "))
print("==========================")
# Criando os objetos (instâncias)
animal1 = validaQuemEQuem(leitura1,vida1)
animal2 = validaQuemEQuem(leitura2,vida2)
# Iniciando a batalha
batalha(animal1, animal2)
print("=============Fim=============")