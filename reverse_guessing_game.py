from logo import logo
import random


print(logo)

print("""Vítejte v hádací hře. 
Myslete si číslo od 1 do 100 a počítač se ho bude snažit uhodnout.""")

repeat_print = ("""

Uhodl? Zvolte jednu z následujících možností:
1 - Počítač uhodl
2 - Číslo je příliš NÍZKÉ
3 - Číslo je příliš VYSOKÉ\n\n""")

list_min = [0]
list_max = [101]
computer_guess = random.randint(max(list_min) + 1, min(list_max) - 1)
lives = 7
print(f"\n\nTip počítače je {computer_guess}.")

while lives != 0:
    user_help = int(input(repeat_print))
    if user_help == 2:
        list_min.append(computer_guess)
    elif user_help == 3:
        list_max.append(computer_guess)
    elif user_help == 1:
        print("Počítač uhodl Vaše číslo a vyhrál")
        break
    computer_guess = random.randint(max(list_min) + 1, min(list_max) - 1)
    lives -= 1
    if lives == 0:
        print("Počítač vyčerpal všechny pokusy a číslo neuhodnul. Hra končí.")
        break
    print(f"\nPočítač má ještě k dispozici {lives} pokusů.")
    print(f"Nový tip počítače je číslo {computer_guess}")

        