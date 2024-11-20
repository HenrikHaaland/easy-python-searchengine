from colorama import init, Fore, Style

# Initialize colorama
init()

def read_file_and_search(word_to_search, file_name):
    try:
        with open(file_name, "r") as file:
            found_words = []
            word_printed = False  # To ensure the message is printed only once

            for line_number, line in enumerate(file, start=1):  # Hent linjenummer
                words = line.split()
                if word_to_search in words:  # checks if the word is in the line
                    found_words.append(word_to_search)
                    if not word_printed:
                        print("¤----------------------------")
                        print(f"|The word '{word_to_search}' is in the text")
                        word_printed = True #allows the next message to be printed multipul times

                    # markes the word in green and the rest of the line in yellow
                    highlighted_line = ""
                    for word in words:
                        if word == word_to_search:
                            highlighted_line += f"{Fore.GREEN}{word}{Style.RESET_ALL} "
                        else:
                            highlighted_line += f"{Fore.RED}{word}{Style.RESET_ALL} "

                    print(f"|Line {line_number}: {highlighted_line.strip()}")
            return found_words

    except FileNotFoundError:
        print(f"|The file '{file_name}' was not found.")
        return []

# Velg fil
print("¤----------------------------¤")
print("|Choose a file to search in: |")
print("|1. file1.txt                |")
print("|2. file2.txt                |")
print("|3. file3.txt                |")
print("|4. file4.txt                |")
print("¤----------------------------¤")

file_choice = input("|Choose 1, 2, 3 or 4 for their respected files: ")

# Map valg til filnavn
file_mapping = {
    "1": "file1.txt",
    "2": "file2.txt",
    "3": "file3.txt",
    "4": "file4.txt"
}

file_name = file_mapping.get(file_choice)
if not file_name:
    print("Invallid choise. Please start the program anew.")
else:
    # Velg søkeord
    search_word = input(f"|You choose the file '{file_name}'. Write the word you want to search for: ")
    found = read_file_and_search(search_word, file_name)

    if not found:
        print(f"|The word '{search_word}' was not found in the file '{file_name}'.")
    else:
        print(f"|Found {len(found)} cases of '{search_word}' in the file '{file_name}'.")
        print("¤----------------------------")
