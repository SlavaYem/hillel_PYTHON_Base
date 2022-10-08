import random
import string
import json



def generate_alphanum_random_string(length_1):
    letters_and_digits = string.ascii_letters + string.digits + string.whitespace
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(length_1))
    return rand_string


def generate_txt_file(length_2):
    my_str = generate_alphanum_random_string(length_2)
    return my_str


length = random.randint(100, 1001)


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    my_value = random.randint(1, 3)
    if my_value == 1:
        value = random.randint(-100, 100)
    elif my_value == 2:
        value = random.uniform(0, 1)
    else:
        value = random.choice([False, True])
    return value


def generate_json_data():
    return {random_key(): random_value() for _ in range(random.randint(5, 20))}


my_dict = generate_json_data()


def generate_and_write_file(filename):
    if filename.endswith('.txt'):
        with open(filename, "w") as file:
            file.writelines(generate_txt_file(length))
    elif filename.endswith('.json'):
        with open(filename, 'w') as json_file:
            json.dump(my_dict, json_file)
    else:
        print("Unsupported file format")


my_str_1 = "1.json"
my_str_2 = "1.txt"
my_str_3 = "1.fdsfs"
generate_and_write_file(my_str_2)
