# Strings are sorounden by either single quotes (') or double quotes (").
string1 = 'Hello, wOrld'
string2 = "1234"
string3 = "We're #1!"
string4 = 'I said, "Put it over"'
print(string1)

# Multiline strings
long_string = "This is a long string that spans multiple lines.\
It can be useful for writing long paragraphs of text without \
needing to concatenate multiple strings."

# Strings are a sequence of characters.
# We can get the length of a string using the len() function.
print("String1 length:", len(string1))
print(long_string)

# Indexing
character1 = string2[1]  # Get the second character of string2
print("Second character of string2:", character1)

characters = string1[0:2]
print("First two characters of string1:", characters)

last_characters = string1[-1]  # Get the last character of string1
print("Last character of string1:", last_characters)

# Other useful string stuff
uppercase_string = string1.upper()  # Convert string1 to uppercase
print("Uppercase string1:", uppercase_string)

lowercase_string = string1.lower()  # Convert string1 to lowercase
print("Lowercase string1:", lowercase_string)

a = 42
print(f"The value of the variable a is: {a}, be careful!")  # Using f-string for formatted output

# String concatenation
print(string1 + string2)