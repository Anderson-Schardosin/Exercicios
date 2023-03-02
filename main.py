usuario = input('Digite seu nome:')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo memos 6 caracteres')
else:
    print(f"{usuario:#^50} Voce foi cadastrado no sistema")
