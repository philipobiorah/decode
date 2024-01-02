def decode(message_file):
    """Decodes an encoded message from a text file.

    Args:
        message_file (str): The path to the text file containing the encoded message.

    Returns:
        str: The decoded message.

    Raises:
        FileNotFoundError: If the specified file is not found.
        ValueError: If the file format is invalid.
    """

    try:
        with open(message_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{message_file}' was not found.")

    words = []
    for line in lines:
        number, word = line.strip().split()
        try:
            number = int(number)
            words.append((number, word))
        except ValueError:
            raise ValueError("Invalid file format. Each line should contain a number and a word.")

    words.sort(key=lambda x: x[0])

    decoded_message = []
    row_length = 1
    for i, (number, word) in enumerate(words):
        if i >= row_length:
            decoded_message.append(word)
            row_length += 1

    return " ".join(decoded_message)



message = decode("coding_qual_input.txt")
print(message)