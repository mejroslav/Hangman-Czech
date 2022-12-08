import random
import time
import os

reset = '\033[0m'
bold = '\033[01m'
orange = '\033[33m'
red = '\033[31m'
green = '\033[32m'


translation_table = {
    ord("Á"): ord("A"),
    ord("É"): ord("E"),
    ord("Ě"): ord("E"),
    ord("Í"): ord("I"),
    ord("Ó"): ord("O"),
    ord("Ú"): ord("U"),
    ord("Ů"): ord("U"),
    ord("Ý"): ord("Y"),
    ord("Č"): ord("C"),
    ord("Ď"): ord("D"),
    ord("Ň"): ord("N"),
    ord("Ř"): ord("R"),
    ord("Š"): ord("S"),
    ord("Ť"): ord("T"),
    ord("Ž"): ord("Z"),
}

def remove_diacritics(letter):
    "remove hooks and dashes"
    return letter.translate(translation_table)

def rnd_word(length: int):
    "creates new czech word of the given length"
    with open("slova.txt", "r") as file:
        slova = file.read()
    slova = slova.split("\n")
    word = ""
    while len(word) != length: # keep guessing random word - need improvement!
        word = random.choice(slova).upper()
    return word

def game(word, pokusy):

    word = word.upper() # fixes trouble with small and big letters
    pokusy_zacatek = pokusy
    word_letters = set(remove_diacritics(word))
    used_letters = set()


    while len(word_letters) > 0 and pokusy > 0:
        time.sleep(1)
        os.system("clear")

        if pokusy == 1:
            print("Zbývá ti už jen poslední pokus!")
        elif pokusy == 2:
            print("Zbývají ti jenom 2 pokusy!")
        else:
            print(f"Zbývá ti {pokusy} pokusů.")

        print("Použitá písmena:", " ".join(used_letters))
        word_list = [letter if remove_diacritics(letter) in used_letters else "-" for letter in word]
        print("Hádané slovo:", " ".join(word_list))

        user_letter = input("Hádej písmeno: ").upper()
        user_letter_without_diacritics = remove_diacritics(user_letter)

        if user_letter_without_diacritics in used_letters:
            print("Toto písmeno už jsi použil!")
            continue

        # if not in used_letters:
        used_letters.add(user_letter_without_diacritics)
        if user_letter_without_diacritics in word_letters:
            word_letters.remove(user_letter_without_diacritics)
            print(green + "Správně!" + reset) 
        else:
            pokusy -= 1
            print(red + "Špatně!" + reset)

    print("Hádané slovo bylo:", word)
        
    if word_letters == set() and pokusy > 0:
        print(green + "Vyhrál jsi! " + reset + f"Stačilo ti {pokusy_zacatek - pokusy} z {pokusy_zacatek} pokusů. Gratulujeme a tady máš klíčenku!")
    elif pokusy == 0:
        print("Bohužel ti došly pokusy. " + red + "Prohrál jsi!" + reset)




def main():
    os.system("clear")
    print(bold + orange +"""
             __             
|__| /\ |\ |/ _ |\/| /\ |\ |
|  |/--\| \|\__)|  |/--\| \|

Autor: Mejroslav Burýšek     
                           
Vítej u klasické hry Hangman, kterou v češtině známe pod názvem ŠIBENICE.
""" + reset)
    print("""V této hře budeš hádat neznámé slovo pomocí písmen. 
Používáme českou diakritiku (háčky a čárky).
Písmeno 'ch' se bere jako dvě různá písmena 'c'+'h'. """)
    pause = input("Stiskni <ENTER> pro spuštění.")

    
    while True:
        os.system("clear")

        length = int(input("Zadej, kolik písmen má mít hádané slovo: "))
        pokusy = int(input("Zadej, kolik chceš mít pokusů: "))
        time.sleep(1)
        os.system("clear")
        slovo = rnd_word(length)
        time.sleep(1)
        os.system("clear")
        print("Jdeme na to!")
        time.sleep(2)
        os.system("clear")
        game(slovo, pokusy)

        while True:
            again = input("Chceš hrát znovu? [a/n]").lower()
            if again in {"n", "ne", "nn", "no"}:
                print("Na shledanou někdy příště!")
                exit()
            elif again in {"a", "ano", "y", "yes"}:
                break
            else:
                print("Zadej prosím odpověď ('a' = ano, 'n' = ne).")


if __name__ == '__main__':
    main()
