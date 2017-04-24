"""
Currently not working, Still trying to figure out what to grab and check for. Alot of unecessary things are in the code
such as writing the html to a document. Plan to clean it up later
"""
import urllib2
import HTMLParser

class StreamParse(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
	
	def handle_starttag(self, tag, attr):
		x = 0
		if tag == "script":
			x += 1
		print x
		print attr
parse = StreamParse()
request = urllib2.Request("http://api.twitch.tv/kraken/channels/460177396")
response = urllib2.urlopen(request)
html = response.read()
f = open("test.html","r+")
f.write(html)

print html
parse.feed(html)
