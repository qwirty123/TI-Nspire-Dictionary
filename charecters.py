"""
This I used in conjunction with find-and-replace to get rid of special characters; AI script
"""

def find_unique_chars_in_file(filename):
    """
    This function reads a file and prints the unique characters in the text.

    Args:
      filename: The name of the file to read.

    Returns:
      None
    """
    # Open the file in read mode with UTF-8 encoding to handle various characters
    with open(filename, 'r') as file:
        # Read the entire file content into a string
        text = file.read()

    # Convert the text to a set to get unique characters
    unique_chars = set(text)

    # Print each unique character
    for char in sorted(unique_chars):
        print(char, end="")


# Example usage
filename = "dictionaryv.txt"
find_unique_chars_in_file(filename)