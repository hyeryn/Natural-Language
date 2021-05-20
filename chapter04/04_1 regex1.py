import re

def text_match(text, patterns):
    if re.search(patterns, text):
        return('일치하는 항목을 찾았습니다')
    else:
        return('일치하지 않음')

print(text_match("ac","ab?")) #a뒤에 0 또는 b
print(text_match("abc","ab?"))
print(text_match("abbc","ab?"))

print(text_match("ac","ab*")) #a뒤에 0 또는 b
print(text_match("abc","ab*"))
print(text_match("abbc","ab*"))

print(text_match("ac","ab+")) #a뒤에 1개 이상의 b
print(text_match("abc","ab+"))
print(text_match("abbc","ab+"))

print(text_match("abbc","ab{2}")) #a뒤에 2개 이상의 b
print(text_match("aabbbbc","ab{3,5}?"))