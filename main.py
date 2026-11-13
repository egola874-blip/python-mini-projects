
print("\n======== ADVANCED TEXT ANALYZER ========")

input_text = input("Enter your paragraph: ")

# 1. Original Text
print("\n======== ORIGINAL TEXT ========")
print(f"Original Text: {input_text}")

# 2. Case Conversion
print("\n======== CASE CONVERSION ========")
print(f"Uppercase: {input_text.upper()}")
print(f"Lowercase: {input_text.lower()}")
print(f"Capitalize: {input_text.capitalize()}")
print(f"Title Case: {input_text.title()}")
print(f"Swap Case: {input_text.swapcase()}")
print(f"Casefold: {input_text.casefold()}")

# 3. Text Statistics
print("\n======== TEXT STATISTICS ========")
print(f"Character Count: {len(input_text)}")
print(f"Total Words: {len(input_text.split())}")
print(f"Space Count: {input_text.count(' ')}")
print(f"Occurrence of 'o': {input_text.count('o')}")

# 4. Indexing and Slicing
print("\n======== INDEXING AND SLICING ========")

if input_text:
    print(f"First Character: {input_text[0]}")
    print(f"Last Character: {input_text[-1]}")
    print(f"First Three Characters: {input_text[:3]}")
    print(f"Last Three Characters: {input_text[-3:]}")
    print(f"Reverse Text: {input_text[::-1]}")
else:
    print("No text entered.")

# 5. Searching and Replacing
print("\n======== SEARCH AND REPLACE ========")
print(f"Find 'Python': {input_text.find('Python')}")
print(f"Find last 'o': {input_text.rfind('o')}")
print(f"Count of 'o': {input_text.count('o')}")
print(f"Replace Python with Java: {input_text.replace('Python', 'Java')}")

# 6. Split, Join and Partition
print("\n======== SPLIT, JOIN AND PARTITION ========")
print(f"Split Words: {input_text.split()}")
print(f"Words Joined with Hyphen: {'-'.join(input_text.split())}")
print(f"Partition Result: {input_text.partition('Python')}")

# 7. String Checking
print("\n======== STRING CHECKING ========")
print(f"Is Alphabetic: {input_text.isalpha()}")
print(f"Is Numeric: {input_text.isdigit()}")
print(f"Is Alphanumeric: {input_text.isalnum()}")
print(f"Is Whitespace: {input_text.isspace()}")
print(f"Starts with Hello: {input_text.startswith('Hello')}")
print(f"Ends with !: {input_text.endswith('!')}")
print(f"Is Uppercase: {input_text.isupper()}")
print(f"Is Lowercase: {input_text.islower()}")

# 8. String Operators and Immutability
print("\n======== STRING OPERATORS ========")
print(f"Concatenation: {'Hello' + ' Python'}")
print(f"Repetition: {('Hello ' * 3)}")

word = "Python"
new_word = "J" + word[1:]

print(f"Original String: {word}")
print(f"New String: {new_word}")

# 9. String Trimming
print("\n======== STRING TRIMMING ========")
sample = "   Hello Python   "
print(f"Original: '{sample}'")
print(f"Strip: '{sample.strip()}'")
print(f"Left Strip: '{sample.lstrip()}'")
print(f"Right Strip: '{sample.rstrip()}'")

# 10. String Membership
print("\n======== STRING MEMBERSHIP ========")
print(f"Is Python present? {'Python' in input_text}")
print(f"Is Java absent? {'Java' not in input_text}")

# 11. String Comparison
print("\n======== STRING COMPARISON ========")
word1 = "Python"
word2 = "Python"
word3 = "Java"

print(f"word1 == word2: {word1 == word2}")
print(f"word1 == word3: {word1 == word3}")
print(f"word1 != word3: {word1 != word3}")

# 12. Additional String Methods
print("\n======== ADDITIONAL STRING METHODS ========")
print(f"Center: {word.center(30, '-')}")
print(f"Starts with Python: {word.startswith('Python')}")
print(f"Ends with thon: {word.endswith('thon')}")

# 13. String Validation
print("\n======== STRING VALIDATION ========")
text1 = "Python"
text2 = "12345"
text3 = "Python123"
text4 = "123.45"

print(f"Is Alphabetic: {text1.isalpha()}")
print(f"Is Decimal: {text2.isdecimal()}")
print(f"Is Numeric: {text2.isnumeric()}")
print(f"Is Alphanumeric: {text3.isalnum()}")
print(f"Is Identifier: {'student_name'.isidentifier()}")
print(f"Is Decimal with Dot: {text4.isdecimal()}")

# 14. String Formatting Methods
print("\n======== STRING FORMATTING ========")
number = "25"
filename = "python_notes.txt"

print(f"Zero Fill: {number.zfill(5)}")
print(f"Remove Prefix: {filename.removeprefix('python_')}")
print(f"Remove Suffix: {filename.removesuffix('.txt')}")

# 15. Escape Characters and Raw Strings
print("\n======== ESCAPE CHARACTERS ========")
print("Hello\nPython")
print("Hello\tPython")
print("Backslash: \\")

print("\n======== RAW STRINGS ========")
print(r"Hello\nPython")

print("\n======== PROJECT COMPLETED ========")
