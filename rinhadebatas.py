import random
import time


LIGHT_RED = "\033[1;31m"

LIGHT_BLUE = "\033[1;34m"

RESET = "\033[0m"

F = LIGHT_RED + """
                     FFFFFFFFF
                     F
                     FFFFFFFFF
                     F
                     F
                     F
                    """ + RESET

WIN = LIGHT_BLUE + """                 
        W     W     W       I       NNNN  N
         W   W W   W        I       N  N  N
          W W   W W         I       N   N N
           W     W          I       N    NN
""" + RESET

vida = 20

vida_inimigo = 20

titulo = "Rinha de batatas"

print(" ")
print("-" * 20, titulo, "-" * 20)
time.sleep(2)
print(" ")

batata = ["normal", "asterix", "doce", "inglesa", "podre", "queimada", "radioativa", "baroa", "baraka", "bolinha",
          "frita", "mutante"]

batata_aleatoria = random.choice(batata)

fisico = ["normal", "bombado", "desnutrido", "anao", "poste", "nivel tais carla", "japones", "crianca", "idoso", ]
fisico_aleatorio = random.choice(fisico)

contra_aleatorio = random.choice(batata)

fisico_contra_aleatorio = random.choice(fisico)

print("Vc sera uma Batata", batata_aleatoria, "com o fisico", fisico_aleatorio)
time.sleep(2)

print("E seu inimigo vai lutar com uma Batata", contra_aleatorio, "com o fisico", fisico_contra_aleatorio)
time.sleep(2)

arma = ["punhos", "machado", "lanca", "luva de boxe", "sabre de luz", "espada", "faca de serra", "livro",
        "lapis desapontado", "lapis apontado", "hamburguer de siri", "galho", "pá", "controle remoto",
        "controle de video game", "almofada", "espada de diamante", "espada de netherite"]

arma_contra = ["punho", "machado", "lanca", "luva de boxe", "sabre de luz", "espada", "faca de serra", "livro",
               "lapis desapontado", "lapis apontado", "hamburguer de siri", "planta", "galho", "pá", "controle remoto",
               "controle de video game", "almofada", "salgadinho", "espada de diamante", "espada de netherite"]

arma_aleatoria = random.choice(arma)

arma_contra_aleatoria = random.choice(arma_contra)

print(" ")
print("A sua arma sera,", arma_aleatoria)
time.sleep(2)


print("E do seu inimigo sera", arma_contra_aleatoria)
time.sleep(2)

print(" ")
print(" ")
print("Sua batalha comeca em...")
time.sleep(1)

print(" ")
print(" " * 20, "TRES!")
time.sleep(0.55)

print(" ")
print(" " * 20, "DOIS!")
time.sleep(0.55)

print(" ")
print(" " * 20, " UM!")
time.sleep(0.55)

titulo2 = "LUTEM!"

print(" ")
print("*" * 20, titulo2, "*" * 20)
time.sleep(0.75)

while True:

    while vida <= -1:
        vida = 0

    while vida_inimigo <= -1:
        vida = 0

    desviar = ["nao", "desviar"]
    desviar_contra = ["nao", "desviar"]

    desviar_aleatorio = random.choice(desviar_contra)

    desviar_aleatorio_contra = random.choice(desviar_contra)

    normal = 3

    critico = 5

    fraco = 1

    dano = [normal, critico, normal, fraco, normal]

    dano_aleatorio = random.choice(dano)

    dano_aleatorio_inimigo = random.choice(dano)

    if desviar_aleatorio_contra == "nao":
        vida_inimigo -= dano_aleatorio
        print("Você atacou o inimigo, e tirou ", dano_aleatorio, "de dano |")
        time.sleep(1)
        print("A vida do seu inimigo agora é:", vida_inimigo)

        if vida_inimigo <= 0:
            print(" ")
            print("E depois de uma intensa batalha voce...")
            time.sleep(2)

            titulo4 = LIGHT_BLUE + "VENCEU!!!" + RESET
            print("*" * 20, titulo4, "*" * 20)
            time.sleep(1.5)

            print(WIN)
            break

    if desviar_aleatorio_contra == "desviar":
        print("Você vai tentar atacar o inimigo, mas ele desviou |")
        time.sleep(1)

    if desviar_aleatorio == "nao":
        vida -= dano_aleatorio_inimigo
        print("")
        print(" " * 50, "| O inimigo te atacou e tirou", dano_aleatorio_inimigo, "da dano")
        time.sleep(1)
        print(" " * 50, "Sua vida agora é:", vida)
        print("")

        if vida <= 0:
            print("E depois de uma intensa batalha, voce...")
            time.sleep(2)

            titulo3 = LIGHT_RED + 'Morreu...' + RESET

            print(" ")
            print("*" * 20, titulo3, "*" * 20)
            print(F)

            time.sleep(1)
            break

    if desviar_aleatorio == "desviar":
        print("")
        print(" " * 50, "| O inimigo tentou te atacar mas voce conseguiu desviar")
        time.sleep(1)
        print("")
