def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Parsing the file and storing the number-word pairs
    number_word_pairs = {}
    for line in lines:
        number, word = line.split()
        number_word_pairs[int(number)] = word

    # Constructing the pyramid and identifying the numbers at the end of each line
    pyramid_end_numbers = set()
    step, current_number, total_numbers = 1, 1, max(number_word_pairs.keys())
    while current_number <= total_numbers:
        pyramid_end_numbers.add(current_number)
        current_number += step
        step += 1

    # Extracting the words corresponding to the end numbers of the pyramid
    message_words = [number_word_pairs[number] for number in sorted(number_word_pairs.keys()) if number in pyramid_end_numbers]

    return ' '.join(message_words)

# Example usage
decoded_message = decode('file.txt')
print(decoded_message)
