def save_list_to_file(primes, filename, format_choice):
    try:
        with open(filename, 'w') as f:
            if format_choice == '1':
                f.write(", ".join(map(str, primes)) + '\n')
            elif format_choice == '2':
                f.write(" ".join(map(str, primes)) + '\n')
            elif format_choice == '3':
                f.write("\n".join(map(str, primes)) + '\n')
            elif format_choice == '4':
                f.write(",\n".join(map(str, primes)) + ',\n')
            else:
                raise ValueError("Nieprawidłowy format zapisu")
    except Exception as e:
        print(f"Błąd zapisu do pliku: {e}")
