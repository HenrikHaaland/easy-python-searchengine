def read_file_and_search(word_to_search):
    file_name = input("file1 | file2 | file3")

    try:
        with open(file_name, "r") as file:
            found_words = []
            word_printed = False  # For å skrive meldingen kun én gang
            for line in file:
                words = line.split()
                for word in words:
                    if word == word_to_search:
                        found_words.append(word)
                        if not word_printed:
                            print(f"Ordet '{word}' er i teksten")
                            word_printed = True
            return found_words
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
        return []

# Eksempel på bruk
search_word = input("Skriv inn ordet du vil søke etter: ")
found = read_file_and_search(search_word)

if not found:
    print(f"Ordet '{search_word}' ble ikke funnet i teksten.")
else:
    print(f"Fant {len(found)} tilfeller av '{search_word}' i teksten.")
