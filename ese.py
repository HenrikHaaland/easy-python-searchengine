

def read_file():
    file_name = "text.txt"

    try:
        file = open(file_name)
        print(file.read())
        file.close()
    except FileNotFoundError: 
        print("file not found")

read_file()