def main() :
    limite = int(input("ingrese el numero limite: "))
    contador = 1
    numero = 0

    while limite >= contador :
        fibonacci = numero + contador
        
        if fibonacci == 1 :
            print(str(fibonacci) + " " + str(fibonacci), end = " ")
            numero += 1

        elif limite >= fibonacci :
            numero = contador
            contador = fibonacci
            print(str(fibonacci), end = " ")

        else :
            print("")
            break



if __name__ == '__main__' :
    main()