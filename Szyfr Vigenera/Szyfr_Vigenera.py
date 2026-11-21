# Sprawdzenie poprawności klucza
def sprawdz_klucz(klucz):

    # Lista przechowująca komunikaty o błędach
    error = []

    # Sprawdzenie, czy klucz jest pusty zaraz po wprowadzeniu
    if klucz == "":
        print("\nError: Klucz nie może być pusty!")
        return False

    # Sprawdzenie długości klucza czy jest mniejsza niż 8 znaków
    if len(klucz) < 8:
        error.append(f"Klucz jest za krótki ({len(klucz)} zn.)!")

    # Sprawdzenie, czy klucz zawiera spacje
    if any(znak.isspace() for znak in klucz):
        error.append("Klucz nie może zawierać spacji!")

    # Sprawdzenie, czy klucz zawiera cyfry
    if any(znak.isdigit() for znak in klucz):
        error.append("Klucz nie może zawierać cyfr!")

    # Sprawdzenie, czy klucz zawiera litery spoza ASCII
    if any(znak.isalpha() and not znak.isascii() for znak in klucz):
        error.append("Klucz nie może zawierać liter spoza ASCII!")

    # Sprawdzenie, czy klucz zawiera znaki specjalne
    if any(not znak.isalnum() and not znak.isspace() for znak in klucz):
        error.append("Klucz nie może zawierać znaków specjalnych!")

    # Jeśli lista nie jest pusta, wypisujemy wszystkie komunikaty o błędach
    if error:
        for blad in error:
            print("\nError:", blad)
        return False

    return True


# Pobranie klucza od użytkownika
def pobierz_klucz():

    # Pętla działająca dopóki użytkownik nie poda poprawnego klucza
    while True:
        klucz = input("\nPodaj klucz składający się z minimum 8 liter: ")

        if sprawdz_klucz(klucz):
            return klucz


# Pobranie tekstu od użytkownika
def pobierz_tekst(komunikat):

    # Pętla działająca dopóki użytkownik nie poda niepustego tekstu
    while True:
        tekst = input(komunikat)

        if tekst.strip() != "":
            return tekst

        print("\nError: Tekst nie może być pusty!\n")


# Funkcja logiki szyfrowania i deszyfrowania, która przyjmuje tekst, klucz
# i kierunek (1 dla szyfrowania, -1 dla deszyfrowania)
def logika(tekst, klucz, kierunek):

    # String, który będzie przechowywał wynik szyfrowania lub deszyfrowania
    wynik = ""
    # Konwersja klucza na wielkie litery, aby uprościć obliczenia
    klucz = klucz.upper()
    # Zmienna będzie służyła do śledzenia pozycji w kluczu
    pozycja_klucza = 0

    for znak in tekst:

        # Sprawdzenie, czy znak jest literą i należy do zestawu ASCII
        if znak.isalpha() and znak.isascii():

            # Ustalenie bazy dla wielkich i małych liter
            if znak.isupper():
                baza = ord('A')
            else:
                baza = ord('a')

            # Zmienna przechowująca wartość znaku w zakresie 0-25 (A-Z lub a-z)
            wartosc_tekstu = ord(znak) - baza

            # Obliczenie litery klucza na podstawie pozycji i długości klucza
            litera_klucza = klucz[pozycja_klucza % len(klucz)]
            # Obliczenie wartości litery klucza, aby przesunąć znak w tekście
            wartosc_klucza = ord(litera_klucza) - ord('A')

            # Obliczenie wartości znaku z uwzględnieniem
            # kierunku i ograniczeniem do zakresu 0-25
            nowa_wartosc = (wartosc_tekstu + kierunek * wartosc_klucza) % 26

            # Dodanie znaku do wyniku, konwertując nową wartość na znak ASCII
            wynik += chr(nowa_wartosc + baza)

            # Przesunięcie pozycji, aby w następnym kroku użyć kolejnej litery
            pozycja_klucza += 1

        # Jeśli znak nie jest literą A-Z, dodajemy go bez zmian
        else:
            wynik += znak

    return wynik


# Funkcje szyfrowania i deszyfrowania z odpowiednim kierunkiem
def szyfruj(tekst, klucz):
    return logika(tekst, klucz, +1)


def deszyfruj(tekst, klucz):
    return logika(tekst, klucz, -1)


# Funkcja main, która obsługuje interakcję z użytkownikiem
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

            # Pobranie tekstu jawnego i klucza od użytkownika
            tekst = pobierz_tekst("Podaj tekst jawny: ")
            klucz = pobierz_klucz()

            # Wywołanie funkcji szyfruj i wyświetlenie szyfrogramu
            print("\nSzyfrogram:", szyfruj(tekst, klucz))
            print("\n")
        elif wybor == "2":

            # Pobranie szyfrogramu i klucza od użytkownika
            tekst = pobierz_tekst("Podaj szyfrogram: ")
            klucz = pobierz_klucz()

            # Wywołanie funkcji deszyfruj i wyświetlenie odszyfrowanego tekstu
            print("\nOdszyfrowany tekst:", deszyfruj(tekst, klucz))
            print("\n")
        elif wybor == "3":

            # Wyświetlenie komunikatu o zakończeniu programu i przerwanie pętli
            print("\nKoniec programu.")
            break

        # Wyświetlenie komunikatu o błędzie przy niepoprawnym wyborze
        else:

            print("\nError: Niepoprawny wybór!")
            print("Spróbuj ponownie.")
            print("\n")


# Uruchomienie programu. Ctrl+C lub Ctrl+D kończy go bez błędu
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrzerwano. Koniec programu.")
