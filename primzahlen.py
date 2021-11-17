#Jeldrik Hemme
#ETS 2021
#16.11.2021

#Hardware: Es wird keine Hardware benötigt

#Version:0.2

#Aufgabe: Ermitteln Sie für einen festgelegten Zahlenbereich
#die Primzahlen und schreiben Sie diese in eine Liste. Geben Sie die Liste anschließend aus.

#Aufforderung in der Konsole Werte einzugeben 
erste_zahl = input('Bitte eine Zahl eingeben ')
zweite_zahl = input('Bitte eine Zahl eingeben ')

#Umwandeln der Varibalen in Integer
erste_zahl = int(erste_zahl)
zweite_zahl = int(zweite_zahl)

#Listen für zur Zwischenablage 
primzahlen = []
primzahlen_augeben_1 = []

#Errechnen der Primzahlen über zwei for-Schleifen 
for n in range (erste_zahl,zweite_zahl):            #in n werden nach einander die Werte eingetragen durch die for-Schleife     
    for i in range (2, n):                          #in i werden nach einander die Werte von zwei bis n(-1) eingetragen
     if n % i == 0:                                 #es wird überprüft, ob die Zahl n Modul einer der Zahlen in i 0 ergibt 
         break                                      #wenn der Modulu null ergibt wird die nächste Zahl in n geprüft, mit dem break sprint man wieder in die an den Anfang
    else:
        primzahlen = primzahlen + [n]               #wenn keine der Zahlen Modulu null ergibt wird die Zahl zu der Variable Primzahlen hinzugefügt

#Aussortieren der 1 und alles was unter eins liegt, da es keine Primzahlen sind 
for primzahlen_augeben in primzahlen:
    if primzahlen_augeben > 1 :
        primzahlen_augeben_1 = primzahlen_augeben_1 + [primzahlen_augeben]

#Ausgabe der Primzahlen in einer Liste        
for primzahlen_augeben_2 in primzahlen_augeben_1:
    print(primzahlen_augeben_2)

