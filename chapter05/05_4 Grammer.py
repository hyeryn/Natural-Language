import nltk
import string
from nltk.parse.generate import generate

productions = [ #생성순서
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER",
]

digits = list(string.digits)
for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w=digit)) #숫자생성

letters = "' | '".join(list(string.ascii_lowercase)[:4])
productions.append("LETTER -> '{w}'".format(w=letters)) #소문자생성

grammarString = "\n".join(productions)

grammar = nltk.CFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=5, depth=5): #처음 생성되는 5개의 단어
    palindrome = "".join(sentence).replace(" ", "")
    print("Generated Word: {}, Size : {}".format(palindrome, len(palindrome)))