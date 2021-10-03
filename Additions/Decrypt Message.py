def is_prime_number(number):
    if number <= 1:
        return False
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
        if counter > 2:
            return False

    return True


num_of_commands = int(input())
text_to_decrypt = input()

current_decryption = text_to_decrypt

while num_of_commands > 0:
    first_half = ""
    second_half = ""

    for index, element in enumerate(current_decryption):
        position = index + 1
        if is_prime_number(position):
            first_half += element
        else:
            second_half += element

    current_decryption = first_half + second_half
    num_of_commands -= 1

print(current_decryption)
