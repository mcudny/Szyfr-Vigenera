# Szyfr Vigenère’a

## 1. Opis projektu

	Projekt przedstawia implementację klasycznego szyfru Vigenère’a w języku Python.
	Program umożliwia szyfrowanie oraz deszyfrowanie tekstu przy wykorzystaniu klucza podanego przez użytkownika. Aplikacja działa w konsoli i posiada proste menu umożliwiające wybór wykonywanej operacji.

## 2. Funkcjonalności

	- Szyfrowanie tekstu przy użyciu klucza.
	- Deszyfrowanie zaszyfrowanego tekstu przy użyciu klucza.
	- Możliwość samodzielnego ustalenia klucza przez użytkownika.
   	- Wymaganie klucza o minimalnej długości 8 znaków.
	- Walidacja wprowadzanych danych, aby zapewnić poprawność działania programu.
	- Zachowanie oryginalnej wielkości liter w szyfrowanym i deszyfrowanym tekście.
	- Zachowanie spacji i znaków specjalnych w szyfrowanym i deszyfrowanym tekście.
	- Obsługa błędów i komunikaty informujące użytkownika o nieprawidłowych danych wejściowych.
	- Menu główne umożliwiające wybór operacji szyfrowania lub deszyfrowania.
	- Obsługa przerwania programu przez użytkownika.

## 3. Dostępne opcje

	- Szyfrowanie tekstu
		- Użytkownik podaje tekst jawny oraz klucz szyfrujący. Program sprawdza poprawność klucza i szyfruje tekst, wyświetlając wynik na ekranie.
	- Deszyfrowanie tekstu
		- Użytkownik podaje zaszyfrowany tekst oraz klucz deszyfrujący. Program sprawdza poprawność klucza i deszyfruje tekst, wyświetlając wynik na ekranie.
	- Wyjście z programu
		- Korzystając z tej opcji użytkownik może zakończyć działanie programu.

## 4. Zasady dotyczące klucza

    - Klucz musi składać się wyłącznie z liter alfabetu A-Z.
    - Klucz musi mieć minimalną długość 8 znaków.
    - Nie może zawierać spacji ani znaków specjalnych.
	- Nie może zawierać cyfr.
	- Nie może być pusty.
	- Nie może zawierać znaków diakrytycznych (np. ą, ć, ł, ń, ó, ś, ź, ż).
	
	W przypadku niepoprawnego klucza program wyświetli komunikat o błędzie i poprosi użytkownika o ponowne wprowadzenie klucza.

## 5. Zastosowany algorytm szyfrowania

	Szyfr Vigenère’a jest oparty na tablicy Vigenère’a, czyli macierzy liter alfabetu A-Z. Program nie korzysta z tablicy, tylko z równoważnego wzoru arytmetycznego.
	Zostały zastosowane dwa wzory matematyczne do szyfrowania i deszyfrowania:

    Szyfrowanie: C = (P + K) mod 26
	Deszyfrowanie: P = (C - K) mod 26

	Gdzie:

	- C – litera zaszyfrowana (ciphertext)
	- K – litera klucza (key)
	- P – litera tekstu jawnego (plaintext)
	- mod 26 – operacja modulo 26, aby pozostać w zakresie liter alfabetu

	Każdej literze alfabetu przypisana jest wartość liczbową od 0 do 25 (A=0, B=1, C=2, ..., Z=25). W przypadku liter małych, wartości są takie same jak dla liter wielkich. Program zachowuje oryginalną wielkość liter w szyfrowanym i deszyfrowanym tekście.

## 6. Obsługa znaków specjalnych i spacji

	Program zachowuje spacje oraz znaki specjalne w szyfrowanym i deszyfrowanym tekście. Oznacza to, że podczas szyfrowania i deszyfrowania, spacje i znaki specjalne nie są modyfikowane i pozostają na swoich miejscach w tekście.
	W praktyce:

	- Cyfra 0-9 pozostaje cyfrą 0-9 w szyfrowanym i deszyfrowanym tekście.
	- Znaki niebędące literami nie przesuwają pozycji w kluczu.
   	- Spacje w tekście jawnym pozostają spacjami w tekście zaszyfrowanym.
	- Znaki specjalne w tekście jawnym pozostają znakami specjalnymi w tekście zaszyfrowanym.
	- Litery wielkie w tekście jawnym pozostają literami wielkimi w tekście zaszyfrowanym.
	- Litery małe w tekście jawnym pozostają literami małymi w tekście zaszyfrowanym.
	- Znaki diakrytyczne (np. ą, ć, ł, ń, ó, ś, ź, ż) również pozostają niezmienione w szyfrowanym i deszyfrowanym tekście.

## 7. Struktura programu

	- `sprawdz_klucz()` - Weryfikuje poprawność klucza.
	- `pobierz_klucz()` - Pobiera klucz od użytkownika.
	- `pobierz_tekst()` - Pobiera tekst i sprawdza, czy nie jest pusty.
	- `logika()` - Realizuje główny algorytm szyfrowania i deszyfrowania.
	- `szyfruj()` - Wywołuje algorytm w trybie szyfrowania.
	- `deszyfruj()` - Wywołuje algorytm w trybie deszyfrowania.
	- `main()` - Odpowiada za menu i komunikację z użytkownikiem.