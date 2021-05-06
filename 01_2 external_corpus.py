# 임포트
from nltk.corpus import CategorizedPlaintextCorpusReader

# 말뭉치 읽어오기
reader = CategorizedPlaintextCorpusReader(r'C:\Users\hyery\Python-NLP\chaper01\Reviews\tokens',
                                             r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

# 각 카테고리의 샘플을 포함하는 목록 작성
posFiles = reader.fileids(categories='pos')  # 카테고리의 이름을 인수로 받는 fileids()함수
negFiles = reader.fileids(categories='neg')

# 각 목록에서 임의로 파일을 선택
from random import randint

fileP = posFiles[randint(0, len(posFiles) - 1)]
fileN = negFiles[randint(0, len(negFiles) - 1)]
print(fileP)
print(fileN)

# 선택한 파일에 엑세스를 해 문장을 출력
for w in reader.words(fileP):
    print(w+' ', end='')
    if (w is '.'):
        print()

for w in reader.words(fileN):
    print(w+' ', end='')
    if (w is '.'):
        print()