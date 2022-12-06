# modul, který pracuje s databází
# v seznamu "slova" jsou česká slova
file = "syn2015_lemma_abc_utf8.tsv"
with open(file, "r") as r:
    text = r.read()
text = text.split()
slova = text[1::3]

with open("slova.txt", "w") as s:
    for i in slova:
        s.write(i + "\n")