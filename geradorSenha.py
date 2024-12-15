import random 
import string

tamanho = int(input("Digite o valor de caracteres da sua senha: "))

def gerarSenha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senhaGerada = gerarSenha()
print(senhaGerada)