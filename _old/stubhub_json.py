import json

with open("http://www.stubhub.com/ticketAPI/restSvc/event/9394540.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)



#http://www.stubhub.com/ticketAPI/restSvc/event/9394540.json