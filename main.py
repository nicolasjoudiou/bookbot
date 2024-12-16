import string

with open("books/frankenstein.txt") as f:
    # ...

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

num_word=len(file_contents.split())


ref=string.ascii_lowercase
bib_letter={}


for letter in ref:
    bib_letter[letter]=0

for s in file_contents:
    print(s)
    if s in ref:
        bib_letter[s]+=1

#print(bib_letter)

print('-------------This is my report-------------')
print(f"There is {num_word} words in the text")

for letter,value in bib_letter.items():
    print(f"The letter {letter} appears {bib_letter[letter]} times in the text")
   
print("-------------End of my report-------------")