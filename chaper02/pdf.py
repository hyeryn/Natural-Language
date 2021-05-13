from PyPDF2 import PdfFileReader

# 파일을 읽어들여서 PDF 파일의 모든 텍스트를 반환
def getTextPDF(PdfFilename, password=''):
    pdf_file = open(PdfFilename, 'rb') #파일을 읽기 및 역방향 탐색 모드로 연다
    read_pdf = PdfFileReader(pdf_file)
    if password != '':
        read_pdf.decrypt(password) #해당 암호를 이용해 파일 열기 시도
    # 파일에서 텍스트 읽기 작업 시작
    text = []
    for i in range(0, read_pdf.getNumPages()):
        text.append(read_pdf.getPage(i).extractText())
    return '\n'.join(text)