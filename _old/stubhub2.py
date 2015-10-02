import urllib
from lxml import html

url = "http://www.stubhub.com/ticketAPI/restSvc/event/9394540"
page = urllib.urlopen(url)

print page

for i in page:
	print i