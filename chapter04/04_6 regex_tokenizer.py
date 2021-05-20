import re

raw = "I am big! It's the pictures that got small."
print(re.split(r' +', raw)) #띄어쓰기 기준으로 구분

print(re.split(r'\W+', raw)) #단어가 아닌 모든 문자 (' ' , ! )기준으로 구분 -> 결과에서 제거됨

print(re.findall(r'\w+|\S\w*', raw)) #문장부호 살리기