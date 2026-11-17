print("CALCOLO NUOVO ORARIO");

i = 0;

h = -10;
while h < 0 or h > 23:
    h = int(input("Inserire le ore: "));

m = -10;
while m < 0 or m > 59:  
    m = int(input("Inserire i minuti: "));

s = -10;
while s < 0 or s > 59:
    s = int(input("Inserire i secondi: "));

s2 = int(input("Inserire secondi da sommare: "));

print("Orario inziale", h, ":", m, ":", s);

hDiff = s2 // 3600;
mDiff = (s2 // 60) % 60;
sDiff = s2 % 60;

print(hDiff);
print(mDiff);
print(sDiff);

s += sDiff;
mDiff += sDiff // 60;
s = s % 60;

m += mDiff;
hDiff += mDiff // 60;
m = m % 60;

h += hDiff;
if h > 24:
    i = h // 24;
    h = h % 24;

if i > 0:
    giorno = "giorno "+ str(i)
else:
    giorno = "";
    
print("Orario finale:", h, ":", m, ":", s, giorno);

