import urllib
from lxml import html

url = "http://nygeog.github.io/misc/stubhub/stubhub20160101ph.html"
page = urllib.urlopen(url)

print page

for i in page:
	print i