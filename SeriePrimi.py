<<<<<<< HEAD
def IsPrimo(Numero):
    Div = 2;
    while Div < Numero:
        if Numero % Div == 0:
            return False
        Div += 1

    return True



def main():
    print("NUMERO PRIMO")

    Num = 0
    while Num <= 3:
        Num = int(input("Inserire lunghezza sequnza per numeri primi: "))

    print("1, 2", end=", ")
    for i in range(3, Num + 1, 2):
        if IsPrimo(i):
            print(i, end=", ")

main()
    
=======
def IsPrimo(Numero):
    Div = 2;
    while Div < Numero:
        if Numero % Div == 0:
            return False
        Div += 1

    return True



def main():
    print("NUMERO PRIMO")

    Num = 0
    while Num <= 3:
        Num = int(input("Inserire lunghezza sequnza per numeri primi: "))

    print("1, 2", end=", ")
    for i in range(3, Num + 1, 2):
        if IsPrimo(i):
            print(i, end=", ")

main()
    
>>>>>>> 4e002b3504b8608480b5bf45e84172122a79f1e7
