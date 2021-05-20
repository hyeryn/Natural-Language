from bs4 import BeautifulSoup

# html 내용을 첫번쨰 인수로, html.parser를 두번째 인수로 문서를 soup 객체에 로드
html_doc = open('sample-html.html','r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

# soup 객체는 모든 HTML태그를 제거하고 텍스트 내용만 가져와
print('\n\nHTML이 제거된 전체 텍스트:')
print(soup.get_text())

print('<title> 태그에 엑세스:', end=' ')
print(soup.title)

print('<H1> 태그에 엑세스:', end=" ")
print(soup.h1)
print(soup.h1.string) #stirng만 뽑아오기

print('<H1> 태그에 엑세스:', end=" ")
print(soup.img['alt']) #img의 alt속성에 직접 태그

print('\n존재하는 모든 <p>태그에 엑세스:')
for p in soup.find_all('p'):
    print(p.string)