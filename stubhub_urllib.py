import urllib
import time

pauser =   60 #1 minute for testing
pauser = 3600 #an hour
pauser =  450 #7.5 minutes, grab each every half hour

eventList = ['9394538','9394539','9394540','9394541']
dateList  = ['20151230','20151231','20160101','20160102']


for i in range(1,3001):
	for i, j in zip(eventList, dateList):
		theTime = time.strftime("%Y%m%d%H%M")
		print theTime
		urllib.urlretrieve ('http://www.stubhub.com/ticketAPI/restSvc/event/'+i+'.json', 'data/ph'+j+'_'+i+'_'+theTime+'.json')

		time.sleep(pauser)