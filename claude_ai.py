def decode(message_file):
    message = ""
    with open(message_file, 'r') as f:
        lines = f.readlines()
        num_words = 1
        for line in lines:
            words = line.split()
            if len(words) == num_words:
                message += words[-1] + " "
            num_words += 1
    return message.strip()





print(decode("coding_qual_input.txt"))