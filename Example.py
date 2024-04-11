#[username,password,clientcode,ciddata,[messageType,eventQualifier,eventCode,partition,zoneUser],]

from csvAlarmServer import ContactIDServer
allowed_clients = ['1234']
def proc(data):
    if data[2] in allowed_clients and data[4][2] != '602':
        print("Data:  "+str(data))
        print("Event Qualifier: "+server.find_event_quals(data[4][1]))
        print("Event Code: "+server.find_event_description(data[4][2]))
        print("Partition: "+data[4][3])
        print("Zone / User: "+data[4][4])
        print("Client Code: "+data[2])
        print("----------------------------")
        print("----------------------------")

server = ContactIDServer(port=5553, callback=proc)

server.run_server()

