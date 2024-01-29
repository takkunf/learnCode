def main():
    moneda = float(input("""
    Bienvenido al conversor de dolar $ gratis
        1. Peso Boliviano Bs
        2. Yen ¥
        3. Real R$
    Ingrese la opcion de la moneda que desea convertir: """))

    if moneda == 1 :
        valor = float(input("Cuantos Bs desea cambiar a $?: "))
        dolar = valor / 6.9
        print("Su total seria de " + str(dolar) + "$")

    elif moneda == 2 :
        valor = float(input("Cuantos ¥ desea cambiar a $?: "))
        dolar = valor / 109.91
        print("Su total seria de " + str(dolar) + "$")

    elif moneda == 3 :
        valor = float(input("Cuantos R$ desea cambiar a $?: "))
        dolar = valor / 5.32
        print("Su total seria de " + str(dolar) + "$")

    else:
        print("Elige una opcion valida subnormal!")




if __name__ == '__main__':
    main()