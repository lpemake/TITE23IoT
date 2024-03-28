

tiedosto = open("numbers.txt", "r")

# lista numeroita varten
mittaukset = []

for rivi in tiedosto:
    rivi = rivi.rstrip() # rivinvaihto pois
    #print(rivi)
    nopeus = float(rivi)
    mittaukset.append(nopeus)

tiedosto.close()

# lasketaan mittausten keskiarvo
sum = 0
for mittaus in mittaukset:
    #print(mittaus)
    sum += mittaus

keskiarvo = sum / len(mittaukset)
print("keskiarvo:", keskiarvo)