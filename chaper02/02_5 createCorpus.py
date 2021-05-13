import os
import word, pdf
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def getText(txtFileName):
    file = open(txtFileName,'r')
    return file.read()

# 새로운 corpus 폴더 생성-디렉터리
newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):
    os.mkdir(newCorpusDir)

txt1 = getText('sample_feed.txt')
txt2 = pdf.getTextPDF('sample-pdf.pdf')
txt3 = word.getTextWord('sample-one-line.docx')

# 세 문자열 객체의 내용을 디스크에 파일로 작성(쓰기모드)
files = [txt1, txt2, txt3]
for idx, f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt','w') as fout:
        fout.write(f)

# 파일을 저장한 디렉터리에서 plaintext 객체 생성
newCorpus = PlaintextCorpusReader(newCorpusDir,'.*')
print(newCorpus.words()) #0.txt 모든 단어 출력
print(newCorpus.sents(newCorpus.fileids()[1])) #1.txt 문장 출력
print(newCorpus.sents(newCorpus.fileids()[0])) #0.txt 단락별 출력