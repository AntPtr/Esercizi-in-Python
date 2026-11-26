def CaricaVettore():
    v = []
    s = 's'

    while s == 's' or s == 'S':
      num = int(input("Inserire un numero dentro la lista: "))
      v.append(num)
      s = input("Vuoi inserire un altro numero? (S/N)")

    return v

def SlidingWindow(v):
    sw = []
    for i in range (1, len(v) - 1):
        sw.append((v[i - 1] + v[i] + v[i + 1]) / 3.0)
    return sw

def main():
    print("SLIFING WINDOW")
    #v = CaricaVettore()
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("v=", v)
    if len(v) > 3:
        v = SlidingWindow(v)
        print("Applicazione sliding window con media di larghezza 3")
        print(v)
    else:
        print("Lunghezza della lista inferiore a 3")

main()
