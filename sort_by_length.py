"""This is a supporting script for sorting words from 'slova.txt' by length to 'serazena.txt'.
"""


def main():
    with open("slova.txt", "r", encoding="utf-8") as r:
        slova = r.read()
    slova = slova.split("\n")
    slova = sorted(slova, key=len)

    with open("serazena.txt", "w", encoding="utf-8") as w:
        for word in slova:
            if len(word) == 1:
                continue
            w.write(word)
            w.write("\n")
        w.seek(0)
        w.write("# seřazená data")

    with open("serazena.txt", "r+", encoding="utf-8", newline="\n") as w:
        i = 0
        for line in w:
            if len(line) != i:
                w.write("\t#delka{0}".format(i))
                i += 1


if __name__ == "__main__":
    main()
