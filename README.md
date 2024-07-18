# Generowanie Listy Liczb Pierwszych

## Opis projektu

### Temat projektu
Generowanie listy liczb pierwszych w określonym przedziale za pomocą generatorów i list składanych.

### Cel projektu
Celem projektu jest stworzenie programu, który generuje listę liczb pierwszych w zadanym przedziale oraz umożliwia zapisanie tej listy w wybranym formacie do pliku. Program pozwala także na wyświetlenie wygenerowanej listy liczb pierwszych na ekranie.

### Oczekiwane rezultaty
- Wygenerowanie listy liczb pierwszych w określonym przedziale.
- Możliwość zapisu listy liczb pierwszych do pliku w wybranym formacie.
- Wyświetlenie wygenerowanej listy liczb pierwszych na ekranie.

## Funkcjonalności
- Generowanie listy liczb pierwszych w zadanym przedziale.
- Zapis listy liczb pierwszych do pliku w jednym z czterech formatów.
- Wyświetlenie listy liczb pierwszych na ekranie (do 128 znaków).
- Konsolowy interfejs obsługi.

## Instrukcja uruchomienia projektu

1. Sklonuj repozytorium lub skopiuj pliki projektu do lokalnego folderu.
2. Upewnij się, że masz zainstalowanego Pythona w wersji 3.0 lub wyższej.
3. Otwórz terminal w folderze projektu.
4. Uruchom plik `master.py` poleceniem:
    ```bash
    python master.py
    ```
5. Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli.

## Struktura projektu

Projekt składa się z następujących plików:
- `master.py` - główny plik uruchamiający program.
- `module1.py` - moduł zawierający klasę `PrimeGenerator` do generowania liczb pierwszych.
- `module2.py` - moduł zawierający funkcję `save_list_to_file` do zapisywania listy liczb pierwszych do pliku.
- `test.py` - plik zawierający testy jednostkowe dla projektu.

## Technologia użyta w projekcie
- Python 3.0+
- Biblioteka standardowa Pythona

## Analiza wymagań

### Wymagania funkcjonalne
- Generowanie listy liczb pierwszych w określonym przedziale.
- Zapis listy liczb pierwszych do pliku w wybranym formacie.
- Wyświetlenie listy liczb pierwszych na ekranie.
- Obsługa błędów podczas zapisu do pliku.

### Wymagania niefunkcjonalne
- Program powinien być czytelny i modularny.
- Kod powinien być dobrze zorganizowany i udokumentowany.

### Interfejs użytkownika
- Konsolowy interfejs obsługi.

## Implementacja

### Użycie struktury danych
- Lista do przechowywania liczb pierwszych.

### Klasa i wyszukiwanie atrybutów w klasie
- Klasa `PrimeGenerator` do generowania liczb pierwszych.

### Organizacja kodu w modułach
- Moduły `module1.py` i `module2.py` zawierające odpowiednie funkcje i klasy.

### Wykorzystanie błędów i wyjątków
- Obsługa wyjątków podczas zapisywania listy liczb pierwszych do pliku.

### Wykorzystanie generatorów i list składanych
- Generowanie liczb pierwszych za pomocą list składanych.

### Zastosowanie wybranego elementu biblioteki standardowej
- Użycie biblioteki `os` do zarządzania plikami.

## Testowanie

### Testy jednostkowe
- Testy jednostkowe zaimplementowane w pliku `test.py`.

### Wyniki testów
- Wszystkie testy przeszły pomyślnie.

## Wnioski
Projekt spełnia wszystkie wymagania funkcjonalne i niefunkcjonalne. Możliwe usprawnienia projektu mogą obejmować dodanie interfejsu graficznego użytkownika oraz rozbudowę funkcjonalności o dodatkowe opcje generowania liczb.

---

## Autor

Łukasz Rosiński
