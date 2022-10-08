import os
import random
import string


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits + string.ascii_uppercase + string.whitespace
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print(rand_string)


# def generate_txt_file(filename):
#     with open("filename", "w") as file:
#         my_str = generate_alphanum_random_string(length)
#         filename.write("/n".join(my_str))
#     return my_str

# `length = random.randint(100,1001)`


generate_alphanum_random_string(100)