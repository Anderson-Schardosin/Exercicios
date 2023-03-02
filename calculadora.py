while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None


    sair = input('Quer Sair? [s]im ').lower().startswith('s')
    print(sair)
