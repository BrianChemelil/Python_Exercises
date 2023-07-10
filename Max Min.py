def maxmin(numbers):
    if len(numbers) == 0:
        return None, None

    max = min = numbers[0] # initializes the maximum and minimum variables with the first number from the list
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number

    return max, min

# Get input from the user
input_numbers = input("Enter a list of numbers, separated by spaces: ").split() #splits a string into a list

# Convert input strings to integers
input_numbers = [int(num) for num in input_numbers]

# Call the function and print the result
maximum_num, minimum_num = maxmin(input_numbers)
print("The maximum number is:", maximum_num)
print("The minimum number is:", minimum_num)
