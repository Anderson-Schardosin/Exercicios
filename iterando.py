frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual letra deseja colocar em maiusculo? ')

# while contador < 10:
#     print(frase[contador], contador)
#     contador += 1

# ou
# while contador < tamanho_frase:
#     print(frase[contador], contador)
#     contador += 1

# while contador < tamanho_frase:
#     # print(frase[contador], contador)
#     nova_string += frase[contador]
#     contador += 1
#
# print(nova_string)

#colocar letra em maiusculo

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
