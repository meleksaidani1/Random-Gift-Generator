import random
import time

def generate_codes(service, number, file):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code_length = 16
    separator = '-'

    with open(file, 'a') as out:
        for _ in range(number):
            if service == "Visa":
                # Visa specific setup
                code = separator.join(''.join(random.choice(gentype) for _ in range(code_length)) for _ in range(4)) + '\n'
                out.write(code)
                # ...

            elif service == "iTunes":
                # iTunes specific setup
                code = separator.join(''.join(random.choice(gentype) for _ in range(code_length)) for _ in range(4)) + '\n'
                out.write(code)
                # ...

            # Add more services with their specific setups here using elif

print("Hello To Multiple Gift Card Generator")
print("This Script Is Just for educational purpose; use it at your own risk")
total = int(input("How Many Would You Like To Generate? "))

services = [
    "Amazon", "Roblox",
