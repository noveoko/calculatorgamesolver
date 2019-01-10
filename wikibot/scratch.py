import re, json
from bs4 import BeautifulSoup as bs
import spacy

def clean_vocab(string):
    words = string.split()
    big_words = [a for a in words if len(a) > 5]
    new_string = " ".join(big_words)
    return new_string

nlp = spacy.load('en')

sentence = clean_vocab('''Semiosis (from the Greek: σημείωσις, sēmeíōsis, a derivation of the verb σημειῶ, sēmeiô, "to mark") is any form of activity, conduct, or process that involves signs, including the production of meaning. Briefly – semiosis is sign process. The term was introduced by Charles Sanders Peirce (1839–1914) to describe a process that interprets signs as referring to their objects, as described in his theory of sign relations, or semiotics. Other theories of sign processes are sometimes carried out under the heading of semiology, following on the work of Ferdinand de Saussure (1857–1913).''')


token = nlp(sentence)



options = [clean_vocab(a) for a in open('test_files/disambiguation.txt').readlines()]

for option in options:
    opt = nlp(option)
    print(token.similarity(opt))

print('ACID TEST')
tk = nlp('dog')
tk2 = nlp('dog')
print(tk.similarity(tk2))
