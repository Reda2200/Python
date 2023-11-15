#!/usr/bin/env python3
import os
# Implementare il main menu in modalità user friendly
def main():
    while True:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print('\nChe operazione vuoi fare?\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\ne. Esci')
        job = input('Selezione: ')
        if job in ('1', '2', '3', '4'):
            while True:
                try:
                    num1 = float(input("Inserisci il primo numero: "))
                    break
                except ValueError:
                    print("Il numero inserito non è valido")
                    os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                try:
                    num2 = float(input("Inserisci il secondo numero: "))
                    break
                except ValueError:
                    print("Il numero inserito non è valido")

            if job == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Risultato: ', num1+num2)
            if job == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Risultato: ',num1-num2)
            if job == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Risultato: ',num1*num2)
            if job == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    print('Risultato: ',num1/num2)
                except:
                    print('operazione non valida')
        elif job == 'e':
            print('Uscita')
            break
        else:
            print('Selezione non valida')
# execute
if __name__ == '__main__':
    main()