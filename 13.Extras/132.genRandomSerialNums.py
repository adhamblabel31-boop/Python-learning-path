# --------------------------------------------------------
# ! ----------- generate random serial numbers -----------
# --------------------------------------------------------

import string, random

# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)


def gen_serial(count):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # print(all_chars)

    chars_mount = len(all_chars)
    # print(chars_mount)

    serials_list = []
    while 0 < count:
        random_number = random.randint(0, chars_mount - 1)
        random_char = all_chars[random_number]
        serials_list.append(random_char)
        count -= 1
    
    # print(serials_list)
    print("".join(serials_list))

gen_serial(15)
