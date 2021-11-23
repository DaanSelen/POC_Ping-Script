import os
import string

compleetip = ''

def endmess():
    dummy = input("\nU hebt gekozen om het programma af te sluiten!\nVaarwel!\n" + "#" * 90 + "\n")

def samenstellen():
    while True:
        ip_adres1 = input("Typ het eerste gedeelte in van IP-adres: ")
        if ip_adres1.strip().isdigit():
            ip_adres1 = int(ip_adres1)
            if ip_adres1 < 256:
                break
            else:
                print("\nHet moet een getal tussen de 0 en 255 zijn.")
        else:
            print("\nHet moet een getal zijn.")

    while True:
        ip_adres2 = input("Typ het tweede gedeelte in van IP-adres: ")
        if ip_adres2.strip().isdigit():
            ip_adres2 = int(ip_adres2)
            if ip_adres2 < 256:
                break
            else:
                print("\nHet moet een getal tussen de 0 en 255 zijn.")
        else:
            print("\nHet moet een getal zijn.")

    while True:
        ip_adres3 = input("Typ het derde gedeelte in van IP-adres:  ")
        if ip_adres3.strip().isdigit():
            ip_adres3 = int(ip_adres3)
            if ip_adres3 < 256:
                break
            else:
                print("\nHet moet een getal tussen de 0 en 255 zijn.")
        else:
            print("\nHet moet een getal zijn.")

    while True:
        ip_adres4 = input("Typ het vierde gedeelte in van IP-adres: ")
        if ip_adres4.strip().isdigit():
            ip_adres4 = int(ip_adres4)
            if ip_adres3 < 256:
                break
            else:
                print("\nHet moet een getal tussen de 0 en 255 zijn.")
        else:
            print("\nHet moet een getal zijn.")

    ip_adres1 = str(ip_adres1)
    ip_adres2 = str(ip_adres2)
    ip_adres3 = str(ip_adres3)
    ip_adres4 = str(ip_adres4)

    compleetip = ip_adres1 + "." + ip_adres2 + "." + ip_adres3 + "." + ip_adres4
    return compleetip

def main():
    print("Je moet het IP-adres in 4 gedeeltes opdelen en vervolgens hier invullen")
    compleetip = samenstellen()
    while True:
        antwoord = input("\nHet IP-adres wat je hebt samengesteld is: " + compleetip + " klopt dat? y/n ")
        if antwoord == 'y':
            os.system('ping {}'.format(compleetip))
            while True:
                endant = input("\nWil je doorgaan? y/n ")
                if endant == 'y':
                    main()
                elif endant == 'n':
                    break
                print(endant + "is niet een van de antwoorden die hier worden herkend, probeer het opnieuw")
            endmess()
            break
        elif antwoord =='n':
            print("\nJe zal het IP-adres nu opnieuw kunnen instellen.")
            compleetip = samenstellen()
        print(antwoord + "is niet een van de antwoorden die hier worden herkend, probeer het opnieuw")

print("#" * 90 + "\nWelkom bij dit programma!\n")
main()
