from colorama import init, Fore, Style

# Initialize colorama
init()

def read_file_and_search(word_to_search, file_name, mode):
    try:
        with open(file_name, "r") as file:
            found_words = []
            for line_number, line in enumerate(file, start=1):  # Get line number
                words = line.split()
                if word_to_search in words:  # Check if the word is in the line
                    found_words.append(word_to_search)

                    if mode == "1":  # Mode 1: Just print the word found message
                        print("¤----------------------------")
                        print(f"|The word '{word_to_search}' is in the text")
                        print("¤----------------------------")
                        break  # Only print this once and exit
                    elif mode == "2":  # Mode 2: Print each line containing the word
                        highlighted_line = ""
                        for word in words:
                            if word == word_to_search:
                                highlighted_line += f"{Fore.GREEN}{word}{Style.RESET_ALL} "
                            else:
                                highlighted_line += f"{Fore.RED}{word}{Style.RESET_ALL} "
                        print(f"|Line {line_number}: {highlighted_line.strip()}")
                    elif mode == "3":  # Mode 3: Print the total count of the word
                        continue  # Collect occurrences for counting

            if mode == "3":  # After collecting occurrences, print the count
                print(f"|Found {len(found_words)} cases of '{word_to_search}' in the file '{file_name}'.")
            return found_words

    except FileNotFoundError:  # Error message if the file is not found
        print(f"|The file '{file_name}' was not found.")
        return []

# Choose files
print("¤----------------------------¤")
print("|Choose a file to search in: |")
print("|1. file1.txt                |")
print("|2. file2.txt                |")
print("|3. file3.txt                |")
print("|4. file4.txt                |")
print("¤----------------------------¤")

file_choice = input("|Choose 1, 2, 3 or 4 for their respected files: ")

# Assigning numbers to the text files
file_mapping = {
    "1": "file1.txt",
    "2": "file2.txt",
    "3": "file3.txt",
    "4": "file4.txt"
}

file_name = file_mapping.get(file_choice)
# Error message if you write the wrong file name/number
if not file_name:
    print("Invalid choice. Please start the program anew.")
else:
    # Choose functionality mode
    print("¤----------------------------¤")
    print("|Choose functionality:       |")
    print("|1. check word presence      |")
    print("|2. print whole lines        |")
    print("|3. print word count         |")
    print("¤----------------------------¤")
    mode = input("|Choose 1, 2, or 3: ")

    if mode not in ["1", "2", "3"]:
        print("Invalid mode. Please start the program anew.")
    else:
        # Choose search word
        print("¤----------------------------¤")
        search_word = input(f"|You chose the file '{file_name}'. Write the word you want to search for: ")
        found = read_file_and_search(search_word, file_name, mode)

        if mode != "3" and not found:  # Mode 1 and 2 only need this error message
            print(f"|The word '{search_word}' was not found in the file '{file_name}'.")
