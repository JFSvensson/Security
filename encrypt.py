# Function to get the encryption method from the user
def get_encryption_method():
    while True:
        method = input("Choose encryption method (1 for Substitution, 2 for Transposition): ")
        if method in ('1', '2'):
            return int(method)
        else:
            print("Invalid input. Please enter 1 or 2.")

# Function to get the operation from the user
def get_operation():
    while True:
        operation = input("Choose operation (1 for Encryption, 2 for Decryption): ")
        if operation in ('1', '2'):
            return int(operation)
        else:
            print("Invalid input. Please enter 1 or 2.")

# Function to get the secret key from the user
def get_secret_key():
    while True:
        key = input("Enter secret key: ")
        if key.isdigit():
            return int(key)
        else:
            print("Invalid input. Please enter a numeric key.")

# Function to get the file path from the user
def get_file_path():
    return input("Enter the path to the text file: ")

# Function to read the content of a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to write content to a file
def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File written successfully: {file_path}")
    except IOError:
        print(f"Error writing to file: {file_path}")

# Simple Substitution Encryption
def encrypt_substitution(text, key):
    result = ""
    for char in text:
        if char.isalpha(): # Checks if the character is a letter
            shifted = ord(char) + key # Shifts the character by the key
            if char.islower(): # Checks if the character is lowercase
                result += chr((shifted - ord('a')) % 26 + ord('a')) # Wraps the character around if it goes past 'z'
            else:
                result += chr((shifted - ord('A')) % 26 + ord('A')) # Wraps the character around if it goes past 'Z'
        else:
            result += char
    return result

# Simple Substitution Decryption
def decrypt_substitution(text, key):
    return encrypt_substitution(text, -key) # Decrypts by shifting the characters in the opposite direction

# Test the substitution cipher
text_to_encrypt = "Hello, World!"
key = 3
encrypted_text = encrypt_substitution(text_to_encrypt, key)
decrypted_text = decrypt_substitution(encrypted_text, key)
print("----------------------------------------")
print("TESTING")
print("----------------------------------------")
print("Substitution")
print("Original Text:", text_to_encrypt)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
print("----------------------------------------")

# Columnar Transposition Encryption
def encrypt_transposition(text, key):
    columns = ['' for _ in range(key)] # Creates a list of empty strings
    index = 0 # Keeps track of the current column

    for char in text:
        columns[index] += char # Adds the character to the current column
        index = (index + 1) % key # Moves to the next column

    result = ''.join(columns) # Joins the columns into a single string
    return result

# Columnar Transposition Decryption
def decrypt_transposition(text, key):
    num_rows = (len(text) + key - 1) // key # Calculates the number of rows needed using integer division and -1 to round up
    short_columns = key * num_rows - len(text) # Calculates the number of columns that are shorter than the rest
    num_full_columns = key - short_columns # Calculates the number of columns that are full length

    columns = [] # Creates a list of columns
    start = 0 # Keeps track of the start index of the current column
    for _ in range(num_full_columns): # Loops through the full length columns
        end = start + num_rows # Calculates the end index of the current column
        columns.append(list(text[start:end])) # Adds the current column to the list of columns
        start = end # Moves to the next column
    for _ in range(short_columns): # Loops through the short columns
        end = start + num_rows - 1 # Calculates the end index of the current column
        columns.append(list(text[start:end]) + ['']) # Adds the current column to the list of columns
        start = end # Moves to the next column

    rows = [] # Creates a list of rows
    for i in range(num_rows): # Loops through the rows
        row = [column[i] if i < len(column) else '' for column in columns] # Adds the current row to the list of rows
        rows.append(''.join(row)) # Joins the characters in the row into a single string

    result = "".join(rows) # Joins the rows into a single string

    return result

# Test the Columnar Transposition cipher
text_to_encrypt = "Hello, World!"
key_transposition = 4

encrypted_text_transposition = encrypt_transposition(text_to_encrypt, key_transposition)
decrypted_text_transposition = decrypt_transposition(encrypted_text_transposition, key_transposition)

print("Columnar Transposition")
print("Original Text:", text_to_encrypt)
print("Encrypted Text:", encrypted_text_transposition)
print("Decrypted Text:", decrypted_text_transposition)
print("----------------------------------------")

# Function to get the encryption method from the user
def main():
    encryption_method = get_encryption_method()
    operation = get_operation()
    secret_key = get_secret_key()
    file_path = get_file_path()
    # Read the content of the file
    original_text = read_file(file_path)

    if original_text is not None:
        # Perform encryption or decryption based on user input
        if encryption_method == 1:
            # Substitution encryption/decryption
            processed_text = encrypt_substitution(original_text, secret_key) if operation == 1 else decrypt_substitution(original_text, secret_key)
        elif encryption_method == 2:
            # Transposition encryption/decryption
            processed_text = encrypt_transposition(original_text, secret_key) if operation == 1 else decrypt_transposition(original_text, secret_key)

        # Write the processed content back to the file
        write_file(file_path, processed_text)

    print("Process complete. Check the processed file.")

# Used to ensure the main function is called from the command line
if __name__ == "__main__":
    main()
