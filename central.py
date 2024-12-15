def retornaSoma():
    empty_list = []
    while True:
        entrada = int(input("Digite um valor numerico: "))
        empty_list.append(entrada)
        if entrada == 0:
            break
    return sum(empty_list)

soma = retornaSoma()
print(soma)