def longest(strings):
    if len(strings) == 0:
        return 0

    longest_length = len(strings[0])
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)

    return longest_length

# Get input from the user
input_strings = input("Enter a list of strings, separated by spaces: ").split()

# Call the function and print the result
longest_length = longest(input_strings)
print("The length of the longest string is :", longest_length)
