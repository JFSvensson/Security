import matplotlib.pyplot as plt

def simple_hash(input_data):
    if not isinstance(input_data, str): # Checks if the input is a string
        input_data = str(input_data)
    input_data = input_data.encode('utf-8') # Converts the input to bytes using UTF-8 encoding

    hash_value = sum(input_data) % 256 # Sums the byte values and performs a modulo operation
    return hash_value

# Test the simple hash function
input_data = "Fredriks input"
hash_result = simple_hash(input_data)

print(f"Input: {input_data}")
print(f"Hash Value: {hash_result}")

# Uniformity Test
inputs = [str(i) for i in range(10000)] # Creates a list of strings
hash_values = [simple_hash(input_data) for input_data in inputs] # Creates a list of hash values
plt.hist(hash_values, bins=256) # Creates a histogram of the hash values
plt.title('Uniformity Test - Simple Hash') 
plt.show()

# Avalanche Test
input_pairs = [(i, i ^ 0b1) for i in range(9999)] # Creates a list of pairs of numbers that differ by one bit
hash_differences = [abs(simple_hash(str(pair[0])) - simple_hash(str(pair[1]))) for pair in input_pairs] # Creates a list of hash differences
plt.hist(hash_differences) # Creates a histogram of the hash differences
plt.title('Avalanche Test - Simple Hash')
plt.show()
