# Iznos novca u bankomatu
balans = 5000

# Print je funkcija koju sam korisio za prikaz datih stringova
print("Dobro došli na bankomat, izaberite opciju"
      "1. Balans"
      "2. Povlačenje"
      "3. Depozit"
      "4. Izlaz"
      
      "")
# While petlja izvršava kod sve dok je uslov tačan
while True:

    # Korisnik unosi transkaciju
    opcija = int(input("Unesite transkaciju: "))

    # Ako je opcija jednaka sa 1
    if opcija == 1:
        print("Tvoj balans je: ", balans)
        # Deklarisao sam varijablu drugatransakcija
        drugatranskacija = input("Želite li još jednu transkaciju? Da/Ne: ")

        # Ako je drugatranskacija jednako sa DA
        if drugatranskacija == "Da":
            continue
        else:
            # Ovaj kod se izvršava ako je uslov while petlje netačan
            break

    # Unosimo iznos za povlačenje
    elif opcija == 2:
        povlacenje = float(input("Unesite iznos za povlačenje: "))

        # Ako je balans veći od povlaćenja
        if(balans > povlacenje):
            # Total je stanje računa nakon oduzetog iznosa
            total = balans - povlacenje

            print("Prihvaćeno")
            print("Tvoj novi balans je: ", total)
        else:
            # Ovaj kod se izvrašava ako je uslov while petlje netačan
            print("Nedovoljan balans na računu")

    # Opcija 3, depozit novca. Imamo mogućnst da unesemo iznos novca.
    elif opcija == 3:
        depozit = float(input("Unesite iznos za depozit: "))
        totalbalans = balans + depozit
        print("Prihvaćeno")
        print("Trenutni balans sada je: ", totalbalans)

    # Izlaz(Exit)
    elif opcija == 4:
        print("Izlaz iz programa...")
        exit()

    else:
        # Ovaj kod se izvršava ako je uslov while petlje netačan
        print("Nema odabrane transakcije ")
