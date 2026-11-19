def GiorniMese(n):
    giorniMese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return giorniMese[n - 1]

def Bisestile(anno):
    return (anno % 4 == 0) and (anno % 100 != 0) or (anno % 400 == 0)

def ErroreGiorniMese(giorni, mesi):
    if giorni <= GiorniMese(mesi):
        return False #Non ce errore
    else:
        return True

def ErroreData(giorni, mesi, anni):
    if not(Bisestile(anni)) and mesi == 2:
        if giorni == 29:
            return True #errore 29 febbraio bisestile
    else:
        return False
            
    
def InsertData():
    giorni = 40
    mesi = 40
    anni = -10
    
    print("Inserire una dara nel intervallo 01/01/1990 e 31/12/2030")
    while giorni <= 0 or giorni > 31:
        giorni = int(input("Inserire giorno: "))
                     
    while mesi <= 0 or mesi > 12:
        mesi = int(input("Inserire mese: "))

    while anni < 1990 or anni > 2030:
        anni = int(input("Inserire anno: "))

    if ErroreGiorniMese(giorni, mesi) or ErroreData(giorni, mesi, anni):
        print("Data Inserita non compresa nell intervallo")
        giorni = 40
        mesi = 40
        anni = -10
    else:
        return giorni, mesi, anni
   
def OrdData(giorno, mese, anno):
    if mese == 1:
        return giorno
    else:
        passati = 0
        for i in range(1, mese ):
            passati += GiorniMese(mese)
        passati += GiorniMese(mese) - giorno
        if Bisestile(anno) and mese <= 2:
            mancanti += 1
        return passati

def EndData(giorno, mese, anno):
    if mese == 12:
        return 31 - giorno
    else:
        mancanti = 0
        for i in range(12, mese, -1):
            mancanti += GiorniMese(mese)
        mancanti += GiorniMese(mese) - giorno
        if Bisestile(anno) and mese <= 2:
            mancanti += 1
        return mancanti

def IncrementMese(mese, anno):
    if mese == 12:
        mese = 1
        anno += 1
    else:
        mese += 1
    return mese, anno

def DecrementMese(mese, anno):
    if mese == 1:
        mese = 12
        anno -= 1
    else:
        mese -= 1
    return mese, anno

def SommaData(giorno, mese, anno, giorniDaSommare):
    Diff = GiorniMese(mese) - giorno
    
    if mese == 2 and Bisestile(anno):
        Diff += 1
        
    if giorniDaSommare < Diff:
        return giorniDaSommare + girono, mese, anno
    else:
        giorniDaSommare -= Diff
        mese, anno = IncrementMese(mese, anno)
        giorno = 1

        while giorniDaSommare > 31:
            giorniDaSommare -= GiorniMese(mese)
            if mese == 2 and Bisestile(anno):
                giorniDaSommare -= 1    
            mese, anno = IncrementMese(mese, anno)
            
        if giorniDaSommare > GiorniMese(mese):
            giorniDaSommare -= GiorniMese(mese)
            mese, anno = IncrementMese(mese, anno)
            
    giorno = giorniDaSommare
    return giorno, mese, anno

def SottraiData(giorno, mese, anno, giorniDaScalare):
    if giorniDaScalare < giorno:
        return giorniDaScalare - girono, mese, anno
    else:
        giorniDaScalare -= giorno
        mese, anno = DecrementMese(mese, anno)

        while giorniDaSommare > 31:
            giorniDaSommare -= GiorniMese(mese)
            if mese == 2 and Bisestile(anno):
                giorniDaSommare -= 1           
            mese, anno = DecrementMese(mese, anno)
            
        if giorniDaSommare > GiorniMese(mese):
            giorniDaScalare -= GiorniMese(mese)
            mese, anno = DecrementMese(mese, anno)
            
    giorno = GiorniMese(mese) - giorniDaSommare
    return giorno, mese, anno

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

def DiffData(giorno1, mese1, anno1, giorno2, mese2, anno2):
    if anno1 == anno2:
        if mese1 == mese2:
            return(giorno1 - giorno2)
        elif mese1 > mese2:
            return CalcolaDiffGMese(giorno1, mese1, anno1, giorno2, mese2, anno2)
        else:
            return CalcolaDiffGMese(giorno2, mese2, anno2, giorno1, mese1, anno1)
    elif anno1 > anno2:
        return CalcolaDiffGAnno(giorno1, mese1, anno1, giorno2, mese2, anno2)
    else:
        return CalcolaDiffGAnno(giorno2, mese2, anno2, giorno1, mese1, anno1)


def main():
    print("CALCOLATRICE DI DATE")
    i = 0
    while i != 6:
        print("\t\tMENU")
        print("1. Numero dei giorni passati dall inizio dell'anno")
        print("2. Numero dei giorni che mancano alla fine dell'anno")
        print("3. Distanza tra due date")
        print("4. Sommare giorni ad una data")
        print("5. Sottrarre giorni ad una data")
        print("6. Uscire")
        i = int(input("\nInserire la scelta: "))

        if i == 1:
            giono, mese, anno = InserData()
            print("Il numero di giorni passati dal 01/01: ", OrdData(giorno, mese, anno))
        elif i == 2:
            giono, mese, anno = InserData()
            print("Il numero di giorni mancanti al 31/12: ", EndData(giorno, mese, anno))
        elif i == 3:
            print("Prima data")
            giono, mese, anno = InserData()
            print("Seconda data")
            giono1, mese1, anno1 = InserData()
            print("Il numero di giorni mancanti al 31/12: ", DiffData(giorno, mese, anno))
        elif i == 4:
            giorno, mese, anno = InsertData():
            dd = int(input("Inserire il numero di giorni da sommare alla data :"))
            print("La nuova data e: ", SommaData(giorno, mese, anno))
        elif i == 5:
            giorno, mese, anno = InsertData():
            dd = int(input("Inserire il numero di giorni da sottrarre alla data :"))
            print("La nuova data e: ", SottraiData(giorno, mese, anno))
        elif i == 6:
            print("Programma terminato")
        else:
            print("Scelta non valida")

    print("")
    
main()

    
