empty_list = []
a = 0
b = 1
empty_list.append(a)
entrada = int(input("Digite o tamanho do range: "))

for i in range(entrada):
    a, b = b, a
    a += b
    empty_list.append(a)
print(empty_list)