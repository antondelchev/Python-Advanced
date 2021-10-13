def convert_message(message):
    vowels = "aeiouAEIOU"
    message = list(message)
    for el in vowels:
        while el in message:
            message.remove(el)
    message = "".join(message)
    return message
