def primo(numero) :
    contador = 0
    divisor = 0
    
    while numero >= divisor :
        divisor += 1
        if numero % divisor == 0 :
            contador += 1
        elif contador > 2 :
            break
        else :
            continue

    if contador == 2 :
        return True

    else :
        return False

def main():
    numero = float(input("Ingresa un numero: "))
    esPrimo = primo(numero)
    
    if esPrimo == True :
        print("Es norteño xd!")

    else :
        print("No es norteño xc ")
    
    
if __name__ == '__main__': 
    main()