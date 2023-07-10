def vowels(string): #takes a string as input
    vowels = "aeiouAEIOU"
    count = 0

    for char in string: #iterates through each character of the string
        if char in vowels:
            count += 1

    return count

# Get input from the user
inputStrings = input("Enter anything: ")

# Call the function and print the result
num_vowels = vowels(inputStrings)
print("The number of vowels in what you entered are:", num_vowels)
