from html.parser import HTMLParser
import feedparser
from urllib.parse import quote

imgsrc = []

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if attrs:
            if attrs[0][0] == 'src':
                imgsrc.append(attrs[0][1])

            if attrs[0][0] == 'href':
                if 'https://www.flickr.com/photos' in attrs[0][1]:
                    imgsrc.append(attrs[0][1])
                    urlenc = quote(attrs[0][1],safe='') #urlencoded url for facebook likes.
                    imgsrc.append(urlenc)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def feedParser(url_str, search_text):
    global imgsrc
    imgsrc = []

    rss_url = url_str + search_text #Flickr feed API

    feed_url = feedparser.parse(rss_url)

    if feed_url['entries']:
        content = feed_url['entries'][1].content

        posts = []

        for x in feed_url['entries']:
            posts.append(x.content[0].value) #get the html of images and sources.

        ptext = MyHTMLParser()

        for x in posts:
            ptext.feed(x) #parse html with img and href.

        return imgsrc
