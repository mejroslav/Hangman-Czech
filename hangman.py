import random
import time
import os

reset = '\033[0m'
bold = '\033[01m'
orange = '\033[33m'
red = '\033[31m'
green = '\033[32m'


# vytvoření náhodného slova a hádanky
def rnd_word(delka: int):
    with open("slova.txt", "r") as file:
        slova = file.read()
    slova = slova.split("\n")
    word = ""
    while len(word) != delka:
        word = random.choice(slova).upper()
    return word



# TODO: odstranit rozlišování diakritiky
def remove_diacritics(letter):
    return letter.translate(translation_table)
translation_table = {
    ord("á"): ord("a"),
    ord("é"): ord("e"),
    ord("í"): ord("i"),
    ord("ó"): ord("o"),
    ord("ú"): ord("u"),
    ord("ů"): ord("u"),
    ord("ý"): ord("y"),
    ord("ě"): ord("e"),
    ord("č"): ord("c"),
    ord("ž"): ord("z"),
    ord("š"): ord("s"),
    ord("ť"): ord("t"),
    ord("ň"): ord("n"),
    ord("ď"): ord("d"),
}



def game(word, pokusy):
    pokusy_zacatek = pokusy
    word_letters = set(word) # písmena ve slově
    used_letters = set() # písmena, co byla hádána

    while len(word_letters) > 0 and pokusy > 0:
        os.system("clear") # čištění obrazovky na začátku
        if pokusy == 1:
            print("Zbývá ti už jen poslední pokus!")
        elif pokusy == 2:
            print("Zbývají ti jenom 2 pokusy!")
        else:
            print(f"Zbývá ti {pokusy} pokusů.")
        print("Použitá písmena:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word] # nejzajímavější řádek v celém projektu!
        print("Hádané slovo:", " ".join(word_list))

        user_letter = input("Hádej písmeno: ").upper()
        if user_letter in used_letters:
            print("Toto písmeno už jsi použil!")
            time.sleep(1)
            continue
        # pokud není v použitých písmenech
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(green + "Správně!" + reset) 
        else:
            pokusy -= 1
            print(red + "Špatně!" + reset)
        time.sleep(1)

    print("Hádané slovo bylo:", word)
        
    if word_letters == set() and pokusy > 0:
        print(green + "Vyhrál jsi! " + reset + f"Stačilo ti {pokusy_zacatek - pokusy} pokusů. Gratulujeme a tady máš klíčenku!")
    elif pokusy == 0:
        print("Bohužel ti došly pokusy. " + red + "Prohrál jsi!" + reset)




def main():
    os.system("clear")
    print(bold + orange + "Vítej u hry ŠIBENICE!" + reset)
    time.sleep(3)
    os.system("clear")

    delka = int(input("Zadej, kolik písmen má mít hádané slovo: "))
    pokusy = int(input("Zadej, kolik chceš mít pokusů: "))
    time.sleep(1)
    os.system("clear")
    slovo = rnd_word(delka)
    time.sleep(1)
    print("""Pamatuj, že tahle šibenice bohužel rozlišuje diakritiku.\n(u,ú,ů jsou různá písmena)""")
    time.sleep(3)
    os.system("clear")
    print("Jdeme na to!")
    time.sleep(2)
    os.system("clear")
    game(slovo, pokusy)

if __name__ == '__main__':
    main()


