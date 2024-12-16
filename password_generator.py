#importing the string and random libraray for string manipulation and random for generating random ass pass
import string
import random

def random_password_generator(password_len=12,Use_uppercase = True,Use_numbers = True,Use_symbols = True,):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if Use_uppercase else ""
    numbers = string.digits if Use_numbers else ""
    symbols = string.punctuation if Use_symbols else ""
    if password_len<4:
        raise ValueError("password length should be 4 or greater than 4")


    all_characters = lower + upper + numbers + symbols
    if not all_characters:
        raise ValueError("Atleast one charcter type has to be selected")

    password =[]
    password.append(random.choice(lower))
    if Use_uppercase:
        password.append(random.choice(upper))
    if Use_numbers:
        password.append(random.choice(numbers))
    if Use_symbols:
        password.append(random.choice(symbols))

    length = password_len-len(password)
    password.extend(random.choices(lower, k=length))

    random.shuffle(password)
    return ''.join(password)

def main():
    password_len = int(input("Enter the password length: (atleast 6)"))
    use_uppercase = input("include uppercase:(Y/N)").strip().upper() == "Y"
    use_numbers = input("include numbers:(Y/N)").strip().upper() == "Y"
    use_symbols = input("include symbols:(Y/N)").strip().upper() == "Y"
    password = random_password_generator(password_len,use_uppercase,use_numbers,use_symbols)
    print(f"password_generated :{password}")



main()