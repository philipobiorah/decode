def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    number_word_pairs = {int(line.split()[0]): line.split()[1] for line in lines}

    # Correctly identifying the end numbers of each pyramid row
    pyramid_end_numbers = set()
    step, current_number = 1, 1
    while current_number <= max(number_word_pairs.keys()):
        pyramid_end_numbers.add(current_number)
        step += 1
        current_number += step

    # Extracting the words
    message_words = [number_word_pairs[number] for number in sorted(number_word_pairs.keys()) if number in pyramid_end_numbers]

    return ' '.join(message_words)

# Example usage
decoded_message = decode('coding_qual_input.txt')
print(decoded_message)
