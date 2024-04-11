#CSV-Alarm-Receiver
A Python-based class for handling CSV Alarm IP Receiver operations.

This class is specifically designed and tested for use with ICT's Protege Alarm Panels reporting in CSV IP Mode.

#Usage
To get started, initialize an instance of the ContactIDServer class with the following parameters:

python
Copy code
server = ContactIDServer(BindIP="0.0.0.0", BindPort=65431, CallbackFunction=None)


#Receiving Alarms
When an alarm is received, the specified callback function is triggered with the alarm data as its argument. The data structure returned is as follows:

python
Copy code
DataReturned = [
    username, 
    password, 
    clientcode, 
    ciddata, 
    [messageType, eventQualifier, eventCode, area, zoneUser]
]
Utility Functions
The class also includes two utility functions for retrieving descriptions of event qualifiers and event codes:

python
Copy code
Event Qualifier Description = ContactIDServer.find_event_quals(event_qualifier_id)
Event Code Description = ContactIDServer.find_event_description(event_id)

These functions provide easy access to detailed descriptions based on the event's identifier.
