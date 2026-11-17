print("Giorni un un mese")


def GiorniMese(n):
    giorniMese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return giorniMese[n - 1]

def Bisestile(anno):
    return (anno % 4 == 0) and (anno % 100 != 0) or (anno % 400 == 0)

def CalcolaDiffGMese(gg, gm, ga, lg, lm, la):
    somma_gm = 0
    for i in range(lm + 1, gm):
        somma_gm += GiorniMese(i)
        if i == 2 and Bisestile(ga):
            somma_gm += 1
    somma_gm += gg
    somma_gm += (GiorniMese(lm) - lg)
    return somma_gm

def CalcolaDiffGAnno(gg, gm, ga, lg, lm, la):
    somma_ga = 0
    for i in range(la + 1, ga):
        somma_ga += 365
        if Bisestile(i):
            somma_ga += 1
    somma_ga += CalcolaDiffGMese(31, 12, la, lg, lm, la)
    somma_ga += CalcolaDiffGMese(gg, gm, ga, 1, 1, ga)
    return somma_ga

def main():

    g1 =  int(input("Inseire il giorno prima data: "))
    m1 =  int(input("Inseire il mese prima data: "))
    a1 =  int(input("Inseire l'anno prima data: "))

    g2 =  int(input("Inseire il giorno seconda data: "))
    m2 =  int(input("Inseire il mese seconda data: "))
    a2 =  int(input("Inseire l'anno seconda data: "))

    if a1 == a2:
        if m1 == m2:
            print("La differenza tra le date e di", abs(g1 - g2), "giorni")
        elif m1 > m2:
            print("La differenza tra le date e di", CalcolaDiffGMese(g1, m1, a1, g2, m2, a2), "giorni")
        else:
            print("La differenza tra le date e di", CalcolaDiffGMese(g2, m2, a2, g1, m1, a1), "giorni")
    else:
        if a1 > a2:
            print("La differenza tra le date e di", CalcolaDiffGAnno(g1, m1, a1, g2, m2, a2), "giorni")
        else:
            print("La differenza tra le date e di", CalcolaDiffGAnno(g2, m2, a2, g1, m1, a1), "giorni")

main()
