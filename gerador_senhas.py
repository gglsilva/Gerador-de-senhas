import string
#from itertools import combinations_with_replacement
from random import choice



def gerar_senhas(tipo, tamanho):
    valores = ''
    senha = ''
    
    if tipo == 1:
        valores += string.ascii_letters
    elif tipo == 2:
        valores += string.digits
    elif tipo == 3:
        valores += string.punctuation
    elif tipo == 4:
        valores += string.ascii_letters + string.digits + string.punctuation 
    
    for i in range(tamanho):
        senha += choice(valores)

    print(senha)
    return senha


def salvando_senhas(id, usuario, nova_senha):
    arquivo = open('senhas.txt', 'a')
    arquivo.write("Identificador: {}\n".format(id))
    arquivo.write("Usuario: {}\n".format(usuario))
    arquivo.write("Senha: {}\n".format(nova_senha))
    arquivo.write("\n")
    arquivo.close()
    print('senha salva')


def main():
    id = input("Digite um nome para identificar local da senha: ")
    usuario = input("Digite o nome de usuário: ")
    tamanho = int(input("Digite a quantidade de caracteres que deseja ter na senha: "))
    tipo = int(input('Tipo de Senha: 1-Letras, 2-Numeros, 3-Caractere, 4-Todos'))
    nova_senha = gerar_senhas(tipo, tamanho)
    salvando_senhas(id, usuario, nova_senha)

if __name__ == '__main__':
    print()
    print("-------------------------")
    print("GERADOR DE SENHAS")
    print("-------------------------")
    print()

    main()
