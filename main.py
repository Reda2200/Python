def main():
    print('Che operazione vuoi fare?\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\ne. Esci')
    while True:
        job = input('Selezione: ')
        if job in ('1', '2', '3', '4'):
            num1 = float(input('inserisci il primo numero: '))
            num2 = float(input('Inserisci il secondo numero: '))
            if job == '1':
                print('Risultato: 'num1+num2)
            if job == '2':
                print('Risultato: 'num1-num2)
            if job == '3':
                print('Risultato: 'num1*num2)
            if job == '4':
                print('Risultato: 'num1/num2)
        elif job == 'e':
            print('Uscita')
            break
        else:
            print('Selezione non valida')
# execute
if __name__ == '__main__':
    main()
