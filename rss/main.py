import feedparser
#NewsFeed = feedparser.parse("https://rss.app/feeds/KZ4c2RUyCc6WPJdx.xml")
NewsFeed = feedparser.parse("https://rss.app/feeds/3a6W04TGUVGxCpKu.xml")
entry = NewsFeed.entries[0]

print(entry)
print(type(entry))
print(entry["published"])
