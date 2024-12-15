
import os
import time

def imprimirMensagem():
    mensagem = str(input("Digite uma mensagem: "))
    return mensagem

imprimindo = imprimirMensagem()
print(imprimindo)


time.sleep(1.8)
os.system("cls")

def retornaPar():
    empty_list = []
    entrada = int(input("Digite um valor inteiro: "))
    if entrada % 2 == 0:
        empty_list.append(entrada)
        return empty_list
    else:
        return f"Entrada: {entrada} -> Impar"
    

pares = retornaPar()
print(pares)