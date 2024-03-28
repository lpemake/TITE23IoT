import matplotlib.pyplot as plt
# pip install matplotlib

# avataan tiedosto lukemista varten
tiedosto = open("mittaukset.txt", "r")

# tehdään listat
aikalista = []
painelista = []
lampotilalista = []
kosteuslista = []

# käydään tiedosto läpi rivi riviltä
for rivi in tiedosto:
    rivi = rivi.rstrip()
    #"3 3.5309997308731003 3.9562264309426696 1.5827481957929588"
    osat = rivi.split()
    # ["3", "3.5309997308731003", "3.9562264309426696", "1.5827481957929588"]
    # lisätään tiedot listoihin
    aikalista.append(int(osat[0]))
    painelista.append(float(osat[1]))
    lampotilalista.append(float(osat[2]))
    kosteuslista.append(float(osat[3]))

# plotataan mittaukset ajan suhteen samaan kuvaan
plt.plot(aikalista, painelista)
plt.plot(aikalista, lampotilalista, "r")
plt.plot(aikalista, kosteuslista, "m")
plt.title("Mittaukset")
plt.xlabel("Aika [s]")
plt.ylabel("Paine [mbar]")
plt.show()

