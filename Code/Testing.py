usuario = "Amara asdasd asda s d"
usuario2 = "Milan"





def dividir_entero():
    while True:
        numero1 = int(input())
        numero2 = int(input())
        if numero1 >= numero2:
            numero_grande = numero1
            numero_chico = numero2
        else:
            numero_grande = numero2
            numero_chico = numero1

        if (numero_grande % numero_chico) == 0:

            print("Es division exacta")
        else:
            print("No es division exacta")

dividir_entero()