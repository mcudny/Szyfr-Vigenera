def sprawdz_klucz(klucz):

    error = []

    if klucz == "":
        print("\nError: Klucz nie może być pusty!")
        return False

    if len(klucz) < 8:
        error.append(f"Klucz jest za krótki ({len(klucz)} zn.)!")

    if any(znak.isspace() for znak in klucz):
        error.append("Klucz nie może zawierać spacji!")

    if any(znak.isdigit() for znak in klucz):
        error.append("Klucz nie może zawierać cyfr!")

    if any(znak.isalpha() and not znak.isascii() for znak in klucz):
        error.append("Klucz nie może zawierać liter spoza ASCII!")

    if any(not znak.isalnum() and not znak.isspace() for znak in klucz):
        error.append("Klucz nie może zawierać znaków specjalnych!")

    if error:
        for blad in error:
            print("\nError:", blad)
        return False

    return True


def pobierz_klucz():

    while True:
        klucz = input("\nPodaj klucz składający się z minimum 8 liter: ")

        if sprawdz_klucz(klucz):
            return klucz


def pobierz_tekst(komunikat):

    while True:
        tekst = input(komunikat)

        if tekst.strip() != "":
            return tekst

        print("\nError: Tekst nie może być pusty!\n")


def logika(tekst, klucz, kierunek):

    wynik = ""
    klucz = klucz.upper()
    pozycja_klucza = 0

    for znak in tekst:

        if znak.isalpha() and znak.isascii():

            if znak.isupper():
                baza = ord('A')
            else:
                baza = ord('a')

            wartosc_tekstu = ord(znak) - baza

            litera_klucza = klucz[pozycja_klucza % len(klucz)]
            wartosc_klucza = ord(litera_klucza) - ord('A')

            nowa_wartosc = (wartosc_tekstu + kierunek * wartosc_klucza) % 26

            wynik += chr(nowa_wartosc + baza)

            pozycja_klucza += 1

        else:
            wynik += znak

    return wynik

def szyfruj(tekst, klucz):
    return logika(tekst, klucz, +1)


def deszyfruj(tekst, klucz):
    return logika(tekst, klucz, -1)


def main():

    while True:

        print("-" * 40)
        print("         Szyfr Vigenère'a")
        print("-" * 40)
        print("Dostępne opcje:")
        print("1. Zaszyfruj tekst")
        print("2. Odszyfruj tekst")
        print("3. Wyjście")
        print("-" * 40)
        print("\n")

        wybor = input("Wybierz opcję wpisując odpowiednią cyfrę (1-3). Numer: ").strip()

        if wybor == "1":

            tekst = pobierz_tekst("Podaj tekst jawny: ")
            klucz = pobierz_klucz()

            print("\nSzyfrogram:", szyfruj(tekst, klucz))
            print("\n")
        elif wybor == "2":

            tekst = pobierz_tekst("Podaj szyfrogram: ")
            klucz = pobierz_klucz()

            print("\nOdszyfrowany tekst:", deszyfruj(tekst, klucz))
            print("\n")
        elif wybor == "3":

            print("\nKoniec programu.")
            break

        else:

            print("\nError: Niepoprawny wybór!")
            print("Spróbuj ponownie.")
            print("\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrzerwano. Koniec programu.")
