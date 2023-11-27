import matplotlib.pyplot as plt

def djb2_hash(input_data):
    if not isinstance(input_data, str): # Checks if the input is a string
        input_data = str(input_data).encode('utf-8') # Converts the input to a string and encodes it as UTF-8

    # Calculate the hash value using the djb2 algorithm
    hash_value = 5381
    for char in input_data:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)  # hash * 33 + c

    return hash_value % 256 # Performs a modulo operation

# Test the djb2 hash function
input_data = "Fredriks input"
hash_result = djb2_hash(input_data)

print(f"Input: {input_data}")
print(f"Hash Value: {hash_result}")

# Uniformity Test
inputs = [str(i) for i in range(10000)] # Creates a list of strings
hash_values = [djb2_hash(input_data) for input_data in inputs] # Creates a list of hash values
plt.hist(hash_values, bins=256) # Creates a histogram of the hash values
plt.title('Uniformity Test - djb2 Hash')
plt.show()

# Avalanche Test
input_pairs = [(i, i ^ 0b1) for i in range(99999)] # Creates a list of pairs of numbers that differ by one bit
hash_differences = [abs(djb2_hash(str(pair[0])) - djb2_hash(str(pair[1]))) for pair in input_pairs] # Creates a list of hash differences
plt.hist(hash_differences) # Creates a histogram of the hash differences
plt.title('Avalanche Test - djb2 Hash')
plt.show()
