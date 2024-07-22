import random

def random_uppercase(input_string):
    output_string = ""
    for char in input_string:
        if char.islower() and random.choice([True, False]):
            output_string += char.upper()
        else:
            output_string += char
    return output_string

while(True):   
    input_string = input("Bitte geben Sie eine Zeichenkette in Kleinbuchstaben ein: ")
    result = random_uppercase(input_string)
    print("Ergebnis:", result)