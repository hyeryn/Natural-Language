import feedparser

myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")

print('피드 제목:', myFeed['feed']['title'])
print('포스트 수:', len(myFeed.entries)) #entries-파싱된 피드의 모든 게시물 목록

post = myFeed.entries[0]
print('포스트 제목:', post.title)

content = post.content[0].value
print('콘텐츠 원본:\n', content)