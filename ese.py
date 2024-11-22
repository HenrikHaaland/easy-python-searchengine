from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init()

def read_file_and_search(word_to_search, file_name, mode):
    try:
        with open(file_name, "r") as file:  # Open the file for reading and auto closing
            found_words = []  # creats an emty list/ array
            word_found = False  # Track if the word is found in any line

            for line_number, line in enumerate(file, start=1):  # Loop through lines with line numbers
                words = line.split()  # Split the line into words
                if word_to_search in words:  # Check if the search word is in the line
                    word_found = True  # Mark the word as found
                    found_words.append(word_to_search)  # Add the word to the list of found words

                    if mode == "2":  # Mode 2: Print lines containing the word
                        highlighted_line = ""
                        for word in words:
                            if word == word_to_search:
                                highlighted_line += f"{Fore.GREEN}{word}{Style.RESET_ALL} "
                            else:
                                highlighted_line += f"{Fore.RED}{word}{Style.RESET_ALL} "
                        print(f"|Line {line_number}: {highlighted_line.strip()}")

            # Mode 1: Print a message if the word is present or not
            if mode == "1":
                if word_found:
                    print("¤----------------------------")
                    print(f"|The word '{word_to_search}' is in the text")
                    print("¤----------------------------")
                else:
                    print("¤----------------------------")
                    print(f"|The word '{word_to_search}' is not in the text")
                    print("¤----------------------------")
                return found_words  # Return occurrences

            # Mode 3: Print the total number of times the word appears
            if mode == "3":
                if word_found:
                    print(f"|Found {len(found_words)} cases of '{word_to_search}' in the file '{file_name}'.")
                else:
                    print(f"|The word '{word_to_search}' was not found in the file '{file_name}'.")

            # Mode 4: Print the entire text file with highlighting
            if mode == "4":
                with open(file_name, "r") as full_file:  # Reopen the file to iterate through all lines
                    for line_number, line in enumerate(full_file, start=1):
                        words = line.split()
                        highlighted_line = ""
                        for word in words:
                            if word == word_to_search:
                                highlighted_line += f"{Fore.GREEN}{word}{Style.RESET_ALL} "
                            else:
                                highlighted_line += f"{Fore.RED}{word}{Style.RESET_ALL} "
                        print(f"|Line {line_number}: {highlighted_line.strip()}")

            return found_words  # Return occurrences

    except FileNotFoundError:  # Error handling for when the file doesn't exist
        print(f"|The file '{file_name}' was not found.")
        return []

# --vvv--inputs and such fancy things--vvv--

# Print file selection menu
print("¤----------------------------¤")
print("|Choose a file to search in: |")
print("|1. file1.txt                |")
print("|2. file2.txt                |")
print("|3. file3.txt                |")
print("|4. file4.txt                |")
print("¤----------------------------¤")

# Prompt the user to select a file
file_choice = input("|Choose 1, 2, 3 or 4 for their respective files: ")

# Map menu choices to file names
file_mapping = {
    "1": "file1.txt",
    "2": "file2.txt",
    "3": "file3.txt",
    "4": "file4.txt"
}

# Get the file name based on user input
file_name = file_mapping.get(file_choice)

# Handle invalid file choice
if not file_name:
    print("Invalid choice. Please start the program anew.")
else:
    # Print functionality options menu
    print("¤----------------------------¤")
    print("|Choose functionality:       |")
    print("|1. Check word presence      |")  # Just check if the word is in the text
    print("|2. Print whole lines        |")  # Print lines that contain the word
    print("|3. Print word count         |")  # Count occurrences of the word
    print("|4. Print whole text file    |")  # Print the whole file with colors
    print("¤----------------------------¤")
    
    # Prompt the user to select a mode
    mode = input("|Choose 1, 2, 3, or 4: ")

    # Handle invalid mode choice
    if mode not in ["1", "2", "3", "4"]:
        print("Invalid mode. Please start the program anew.")
    else:
        # Prompt the user to enter the word to search for
        search_word = input(f"|You chose the file '{file_name}'. Write the word you want to search for: ")
        print("¤----------------------------¤")
        
        # Perform the search based on the chosen mode
        found = read_file_and_search(search_word, file_name, mode)

        # Print a message if the word is not found (for modes 2 and 3)
        if mode not in ["1", "4"] and not found:  # Mode 1 and 4 handle this internally
            print(f"|The word '{search_word}' was not found in the file '{file_name}'.")
            print("¤----------------------------")
