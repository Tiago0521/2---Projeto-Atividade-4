# cadastro_animais.py
def cadastrar_animal():
    nome = input("Digite o nome do animal: ")
    idade = input("Digite a idade do animal: ")
    especie = input("Digite a espécie do animal: ")
    print(f"Animal cadastrado: {nome}, Idade: {idade}, Espécie: {especie}")
    
if __name__ == "__main__":
    cadastrar_animal()
