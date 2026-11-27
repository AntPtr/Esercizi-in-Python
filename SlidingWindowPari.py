def CaricaVettore():
    v = []
    s = 's'

    while s == 's' or s == 'S':
      num = int(input("Inserire un numero dentro la lista: "))
      v.append(num)
      s = input("Vuoi inserire un altro numero? (S/N)")

    return v

def SlidingWindow(v, n):
    sw = []
    for i in range(n // 2, len(v) -  n//2):
        somma = 0
        for j in range(i - n//2, i + n//2):
            somma += v[j]
        sw.append(somma/float(n))
    return sw

def main():
    print("SLIDING WINODW")
    v = CaricaVettore()
    n = 2
    while n%2 == 0:
        n = int(input("Inserire dimensioni sliding window(dimensione dispari): "))
    print("v =", v)
    if len(v) > n:
        sw = SlidingWindow(v, n)
        print("Risultato media sliding window di lunghezze", n, ":", sw)
    else:
        print("Dimensione della lista", len(v), " inferiori a sliding window", n)
        
main()
