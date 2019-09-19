import random
import string


def gen_password(string_length):
    """ Generate a random string of fixed length """
    password_string = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_string) for i in range(string_length))


for i in range(10):  # Set desired number of passwords here
    your_pass = gen_password(8)  # Set desired password length here
    print("Your password: " + your_pass)
