def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    number_word_map = {int(line.split()[0]): line.split()[1] for line in lines}
    pyramid_end_numbers, step = set(), 1
    for num in range(1, max(number_word_map.keys()) + 1, step):
        pyramid_end_numbers.add(num)
        step += 1
    message = ' '.join([number_word_map[num] for num in sorted(number_word_map) if num in pyramid_end_numbers])
    return message

# Usage example
decoded_message = decode('coding_qual_input.txt')
print(decoded_message)
