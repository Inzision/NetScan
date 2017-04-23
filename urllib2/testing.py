import HTMLParser

class StreamParse(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
	
	def handle_starttag(self, tag, attr)
		i = 0
		if tag == 'script':
			i += 1
		return i
