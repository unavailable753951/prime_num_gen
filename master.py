import os
from module1 import PrimeGenerator
from module2 import save_list_to_file

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Wybierz opcję:")
    print("1. Generuj listę liczb pierwszych")
    print("2. Wyjście z programu")

def generate_and_handle_primes():
    try:
        start = int(input("Podaj przedział min (int): "))
        end = int(input("Podaj przedział max (int): "))

        generator = PrimeGenerator(start, end)
        primes = generator.generate_primes()

        while True:
            clear_console()
            print("1. Zapisz listę do pliku txt")
            print("2. Wyświetl listę na ekranie (max 128 pierwszych znaków)")
            print("3. Powrót do menu")
            choice = input("Wybierz opcję: ")

            if choice == '1':
                filename = input("Podaj nazwę pliku: ")
                if any(char in filename for char in r'<>:"/\|?*'):
                    print("Nazwa pliku zawiera niedozwolone znaki. Spróbuj ponownie.")
                else:
                    print("W jakim formacie chcesz zapisać liczby?")
                    print("#1. n1, n2, n3, ...\n")
                    print("#2. n1 n2 n3 ...\n")
                    print("#3.\n n1\n n2\n n3\n ...\n")
                    print("#4.\n n1,\n n2,\n n3,\n ...\n")
                    format_choice = input("Wybierz format (1-4): ")
                    save_list_to_file(primes, filename + ".txt", format_choice)
                    print("Lista zapisana do pliku.")
                    input("Naciśnij Enter, aby kontynuować...")
            elif choice == '2':
                clear_console()
                print(f"Lista liczb pierwszych: {primes[:128]}...")
                print("1. Zamknij program")
                print("2. Powrót do menu")
                sub_choice = input("Wybierz opcję: ")
                if sub_choice == '1':
                    exit()
                elif sub_choice == '2':
                    continue
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")
            elif choice == '3':
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
                input("Naciśnij Enter, aby kontynuować...")

    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. Spróbuj ponownie.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    input("Naciśnij Enter, aby kontynuować...")

def main():
    while True:
        clear_console()
        display_menu()
        choice = input("Wybierz opcję: ")
        if choice == '1':
            generate_and_handle_primes()
        elif choice == '2':
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            input("Naciśnij Enter, aby kontynuować...")

if __name__ == "__main__":
    main()
