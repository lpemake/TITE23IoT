import json

tiedosto = open("ehdokkaat.txt", "r")

# lista kaikista ehdokkaista
ehdokkaat = []

for rivi in tiedosto:
    rivi = rivi.rstrip()
    # "Aila	Kivimäki	KOK	92"
    osat = rivi.split()
    #for osa in osat:
    #    print(osa)
    #print("-------------")
    ehdokas = {}
    ehdokas["etunimi"] = osat[0]
    ehdokas["sukunimi"] = osat[1]
    ehdokas["puolue"] = osat[2]
    ehdokas["aanimaara"] = int(osat[3])
    ehdokkaat.append(ehdokas)

tiedosto.close()

# muunnetaan ehdokas-lista json-muotoon
# import json
ehdokkaatJson = json.dumps(ehdokkaat, indent=True)
print(ehdokkaatJson)

# kirjoitetaan json-muotoinen tieto tiedostoon
out = open("ehdokkaat.json", "w")
out.write(ehdokkaatJson)
out.close()

# lasketaan, kuinka monta ääntä kukin puolue saa
# käytetään sanakirjaa
puolueet = {}
# käydään lista ehdokkaista läpi
for e in ehdokkaat:
    # onko ehdokkaan puolue jo sanakirjassa
    puolueenTunnus = e["puolue"]
    if not puolueenTunnus in puolueet:
        #  ei ollut, lisätään puolue sanakirjaan
        # äänet on aluksi 0
        puolueet[puolueenTunnus] = 0
    # lisätään puolueelle ehdokkaan äänimäärä
    puolueet[puolueenTunnus] += e["aanimaara"]

# käydään sanakirja läpi ja tulostetaan puoluiden äänimäärät
for puolue, aanetYht in puolueet.items():
    print(puolue, ":", aanetYht)

# jos halutaan vain tulostaa, voidaan tehdä myös näin
puolueetJson = json.dumps(puolueet, indent=True)
print(puolueetJson)