import math
import random
import time
import requests # pip install requests

# ohjelma simuloi raspberryllä tehtyjä mittauksia

# laskurimuuttuja, joka vastaa kuluvaa aikaa
i = 0

# avataan tiedosto kirjoittamista varten
tiedosto = open("mittaukset.txt", "w")
while i < 100:
    # "olio" mittauksia varten
    measurement = {}
    # nyt luettaisiin antureita
    paine = 10 * math.sin(i/10) + (random.random() * 2 - 1)
    lampotila = 5 * math.cos(i/15) + (random.random() * 2 - 1)
    kosteus = math.sin(i/20) + (random.random() * 4 - 2)
    # laitetaan mittausarvot sanakirjaan
    measurement["api_key"] = "OAVD2O911USTXBJY"
    measurement["field1"] = paine
    measurement["field2"] = lampotila
    measurement["field3"] = kosteus
    print(measurement)
    s = str(i) + " " + str(paine) + " " + str(lampotila) + " " + str(kosteus) + "\n"
    tiedosto.write(s)
    
    # TODO: lähetetään data eteenpäin (ThingsPeakiin tai omalle palvelinsovellukselle)    
    # response = requests.post("https://api.thingspeak.com/update.json", json = measurement)
    response = requests.post("http://localhost:5000/newmeas", json = measurement)
    print(response)
    i += 1
    #time.sleep(16) # Thingspeak vaatii 15 sekunnin viiveen

tiedosto.close()
# tulosta tiedosto käppyröinä matlabilla ja excelillä

# MATLAB:
# >> load c:\temp\mittaukset.txt
# >> plot(mittaukset(:,1), mittaukset(:,2))
# >> hold on
# >> plot(mittaukset(:,1), mittaukset(:,3),'r')
# >> plot(mittaukset(:,1), mittaukset(:,4),'m')
