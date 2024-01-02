def decode(message_file):
    # Open the file and read all lines
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create an empty dictionary to store the number-word pairs
    number_word_pairs = {}
    for line in lines:
        # Split each line into number and word
        parts = line.split()
        number = int(parts[0])
        word = parts[1]
        number_word_pairs[number] = word

    # Create a set to store the numbers at the end of each pyramid row
    pyramid_end_numbers = set()
    
    # Variables to keep track of the current number and the step size
    step = 1
    current_number = 1
    
    # The largest number in our file
    max_number = max(number_word_pairs.keys())

    # Loop to find the end numbers of each pyramid row
    while current_number <= max_number:
        # Add the current number to the set
        pyramid_end_numbers.add(current_number)

        # Increase the step size and update the current number
        step += 1
        current_number += step

    # List to store the words for the final message
    message_words = []

    # Loop through the sorted numbers and pick words from the end numbers
    for number in sorted(number_word_pairs.keys()):
        if number in pyramid_end_numbers:
            message_words.append(number_word_pairs[number])

    # Join the words into a single string and return
    return ' '.join(message_words)

# Using the function
decoded_message = decode('file_input.txt')
print(decoded_message)
