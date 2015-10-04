import json
from pprint import pprint
import urllib2

url = 'http://www.stubhub.com/ticketAPI/restSvc/event/9394540'
url = 'http://www.stubhub.com/ticketAPI/restSvc/event/9394540'
#url = "http://nygeog.github.io/misc/stubhub/stubhub20160101ph.html"

response = urllib2.urlopen(url)
#tickets = data['eventTicketListing']['eventTicket']
html = response.read()
# prices = [ticket['tc']['amount'] for ticket in tickets]
# pprint(sorted(prices))

print response
print 'break'
print html