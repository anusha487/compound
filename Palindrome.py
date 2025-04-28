

def palindrome(string):
    # Remove any spaces and convert the string to lowercase
    string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return string == string[::-1]

# Example usage:
print(palindrome("madam"))  # Output: True
print(palindrome("hello"))  # Output: False
print(palindrome("A man a plan a canal Panama")) 
