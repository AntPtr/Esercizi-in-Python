def CaricaVettore():
    v = []
    s = 's'

    while s == 's' or s == 'S':
      num = int(input("Inserire un numero dentro la lista: "))
      v.append(num)
      s = input("Vuoi inserire un altro numero? (S/N)")

    return v

def Somma(v):
    somma = 0
    for number in v:
        somma += number
    return somma

def Media(v):
    return float(Somma(v) / len(v))

def main():
    print("SOMMA MEDIA LISTA")
    v = CaricaVettore()
    print("La somma dei valori nella lista e' pari a: ", Somma(v))
    print("La media della lista e' pari a :", Media(v))

main()
