print("SEQUENZE CRESCENTI E DECRESCENTI");

Cresc = 0;
Decre = 0;
LenMaxC = 0;
LenMaxD = 0;
LenC = 0;
LenD = 0;
N = 0;

while N <= 1:
    N = int(input("Inserire la lunghezza della sequnza: "));
    
NumPrec = int(input("Inserire il numero n. 1 "));

for i in range(1, N):
    NumSuc = int(input("Inserire il numero n." + str(i + 1) + " : "));
    if NumSuc >= NumPrec:
        if Cresc == 1:
            LenC += 1;
        else:
            Cresc = 1;
            LenC = 2;
    else:
        if Cresc == 1:
            if LenC > LenMaxC:
                LenMaxC = LenC;
            Cresc = 0;

    if NumSuc <= NumPrec:
        if Decre == 1:
            LenD += 1;
        else:
            Decre = 1;
            LenD = 2;
    else:
        if Decre == 1:
            if LenD > LenMaxD:
                LenMaxD = LenD;
            Decre = 0;
    NumPrec = NumSuc;

# Nel caso in cui una sequenza si interrompa per mancaza di numeri succesivi
if LenC > LenMaxC:
    LenMaxC = LenC

if LenD > LenMaxD:
    LenMaxD = LenD

print("La massima sequenza crescente e pari :", LenMaxC, "numeri");
print("Corrispondenti al ", float(LenMaxC)*100 / N, "% della sequenza");

print("La massima sequenza decrescente e pari :", LenMaxD, "numeri");
print("Corrispondenti al ", float(LenMaxD)*100 / N, "% della sequenza");
