import random

intro = "-" * 40
welcome = "{}\n  Welcome to the Password Generator! \n{}".format(
    intro, intro)
print(welcome)


def user_input():
    # ask user for input

    generate_password = input(
        "\n Would you like to generate a random password?: ")

    if generate_password[0].lower() == "y":
        random_password = generate_random_password()

        print("\n Here is your random password, don't share this with no one! ->\n \n{} \n\n{} \n\n{}\n ".format(
            "-"*len(random_password), random_password, "-"*len(random_password)))

        more_complex = input("\n Would you like a more complex password?: ")

        if more_complex[0].lower() == 'y':
            complex_password = "ey" + generate_random_password(70)
            print("\n Here is your complex password ->\n \n{} \n \n{} \n \n{} ".format("-"*len(complex_password),
                  complex_password, "-"*len(complex_password)))
        else:
            return
    else:
        return


def generate_random_password(length=30):
    # GENERATE RANDOM PASSWORD, IN CASE USER FORGOT PASSWORD
    random_password = ""
    random_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+"

    for index in range(length):
        random_password += random_letters[random.randint(
            0, len(random_letters)-1)]
    print("password -> ", random_password)
    return random_password

# generate_random_password()


user_input()
