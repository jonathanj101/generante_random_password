import random


def generate_random_password(length=30):
    # GENERATE RANDOM PASSWORD, IN CASE USER FORGOT PASSWORD
    random_password = ""
    random_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+"
    for letter in range(length):
        random_password += random_letters[random.randint(
            0, len(random_letters)-1)]
    print("password -> ", random_password)
    return random_password
