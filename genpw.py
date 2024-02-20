import random
import string

def generate_special_characters():
    specials = '!@#$%^&*()_-+='
    return random.choice(specials)

def generate_random_name():
    name_length = random.randint(3, 8)
    random_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length))
    return random_name

def generate_all_characters(num_characters):
    characters = string.digits
    result = generate_special_characters()

    result += generate_random_name()

    for _ in range(num_characters - 5 - len(result)):
        result += random.choice(characters)

    result += generate_special_characters()
    return result

def main():
    num_generated = 8
    output_file = "genpw.txt"

    with open(output_file, 'w') as file:
        while True:
            generated_characters = generate_all_characters(num_generated)
            print(generated_characters)
            file.write(generated_characters + '\n')

if __name__ == "__main__":
    main()
